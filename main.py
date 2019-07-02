import itertools
import random

import noir
import story

def has_duplicates(iterable):
    return len(iterable) > len(set(iterable))

class EstablishedIdea:
    def __init__(self, concept, arguments):
        self.concept = concept
        self.arguments = arguments
        assert len(concept.parameters) == len(arguments) 
        assert None not in arguments

    def __str__(self):
        return str(self.concept) + "-" + str(self.arguments)

    def __repr__(self):
        return str(self.concept) + "-" + str(self.arguments)

def get_linked_bound_args(narrative_piece, concept, bound_arguments):
    linked_bound_args = {}
    for parameter in concept.parameters:
        for link_set in narrative_piece.linked_parameters:
            if parameter in link_set:
                for other_param in link_set:
                    if other_param in bound_arguments:
                        existing_val = linked_bound_args.get(parameter)
                        assert existing_val is None or existing_val is bound_arguments[other_param]
                        linked_bound_args[parameter] = bound_arguments[other_param]

    return linked_bound_args

# is the required concept understood from the given established idea and
# arguments we have bound from other understood concepts
def is_established_by(concept, established_idea, bound_arguments):
    if established_idea.concept is not concept:
        return False

    for p_a in zip(concept.parameters, established_idea.arguments):
        if p_a[0] in bound_arguments and bound_arguments.get(p_a[0]) is not p_a[1]:
            return False # This established idea has this same concept but for a
                       # different argument that we have already matched from
                       # another concept in this piece
    return True

def get_established_idea(established_ideas, concept, bound_args):
    for idea in established_ideas:
        if is_established_by(concept, idea, bound_args):
            return idea
    return None

# Return a generator of bound arguments and used_ideas
def get_possible_basis_ideas(narrative_piece, established_ideas):
    def get_randomized_ideas():
        # Randomize so stories with similar beginnings don't always take the
        # same path
        randomized_established_ideas = established_ideas.copy()
        random.shuffle(randomized_established_ideas)
        return randomized_established_ideas

    random_ideas = [get_randomized_ideas() for _ in range(
        len(narrative_piece.required_concepts)
    )]

    for combo in itertools.product(*random_ideas):
        bound_arguments = {}

        used_ideas = []

        for concept, idea in zip(narrative_piece.required_concepts, combo):
            linked_bound_args = get_linked_bound_args(
                narrative_piece, concept, bound_arguments
            )
            if is_established_by(concept, idea, linked_bound_args):
                used_ideas.append(idea)

                for p, a in zip(concept.parameters, idea.arguments):
                    assert p not in bound_arguments
                    bound_arguments[p] = a
            else:
                used_ideas.append(None)

        if any(idea is None for idea in used_ideas):
            continue # we didn't find a good combo of ideas and parameters

        yield (bound_arguments, used_ideas)

def is_prohibited(narrative_piece, established_ideas, bound_arguments):
    for prohibitive_concept_tuple in narrative_piece.prohibitive_concept_tuples:
        #TODO:(we need to bind anything we find in the prohibitive tuple)
        if all(
            get_established_idea(
                established_ideas,
                prohibitive_concept, 
                get_linked_bound_args(
                    narrative_piece, prohibitive_concept, bound_arguments
                )
            )
            is not None for prohibitive_concept in prohibitive_concept_tuple
        ):
            return True # One of the prohibitive concept tuples is already established
    return False

def can_beat_be_used(narrative_piece, established_ideas):
    for bound_arguments, used_ideas in get_possible_basis_ideas(
        narrative_piece, established_ideas
    ):
        if is_prohibited(narrative_piece, established_ideas, bound_arguments):
            continue

        output_bound_args = {}
        for param, arg in bound_arguments.items():
            if param in narrative_piece.input_to_output_params:
                for out_param in narrative_piece.input_to_output_params[param]:
                    output_bound_args[out_param] = arg

        free_parameters = []
        for output_concept in narrative_piece.output_concepts:
            for param in output_concept.parameters:
                if not param in output_bound_args:
                    # A parameter in output but not in inputs, we need to choose a
                    # free arg for this but only if the resulting output concept is
                    # not already established.
                    free_parameters.append(param)

        output_args = None

        all_free_arg_combos_generator = (itertools.product(
            *(noir.free_arguments[param.p_type] for param in free_parameters))
        )

        # This loop goes once if we have 0 free params (with an empty set of args)
        for possible_free_args in all_free_arg_combos_generator:

            output_args = output_bound_args.copy()

            for param, arg in zip(free_parameters, possible_free_args):
                output_args[param] = arg

            found_dup = False

            for output_concept in narrative_piece.output_concepts:
                if output_concept.is_exclusive and has_duplicates(output_args.values()):
                    found_dup = True

            if found_dup:
                # We don't allow selecting the same arg twice if the concept is exclusive
                output_args = None
                continue

            # We don't want to establish the same idea twice otherwise the story scene will seem
            # superflous and redundant
            if any(is_established_by(output_concept, idea, output_args) for idea in established_ideas
                for output_concept in narrative_piece.output_concepts
                ):
                # we have already established this idea so skip to the next possible free args
                output_args = None
            else:
                break # we can establish a new idea with these free args

        # All possible free arg sets lead to already established ideas so skip this bound arg possiblity
        if output_args is None:
            #TODO: in this case I actually need to try the whole thing again with different params from
            # different established ideas
            continue

        newly_established_ideas = []

        for output_concept in narrative_piece.output_concepts:
            output_arguments = [] 
            for param in output_concept.parameters:
                bound_arg = output_args[param]
                assert bound_arg is not None
                output_arguments.append(bound_arg)

            newly_established_ideas.append(EstablishedIdea(output_concept, output_arguments))

        return newly_established_ideas, used_ideas

    return None

def get_ideas_that_have_lead_nowhere(established_ideas, ideas_that_have_lead_to_something):
    return (
        idea for idea in established_ideas
            if not ideas_that_have_lead_to_something.get(idea, False)
    )

def try_update_with_beat(
    narrative_piece, established_ideas, ideas_that_have_lead_to_something
):
    for output_concept in narrative_piece.output_concepts:
        if output_concept is story.story_end:
            # lazily check if there's at least one that has lead nowhere
            if next(get_ideas_that_have_lead_nowhere(
                established_ideas, ideas_that_have_lead_to_something
            ), None) is not None:
                return None

    can = can_beat_be_used(narrative_piece, established_ideas)

    if can is None:
        return None

    ideas_beat_establishes, used_ideas = can

    # Now do the update steps becuase our match was succesful

    established_ideas.extend(ideas_beat_establishes)

    for idea in used_ideas:
        ideas_that_have_lead_to_something[idea] = True

    return [arg for arg in (idea.arguments for idea in ideas_beat_establishes)]

if __name__ == '__main__':
    established_ideas = []
    ideas_that_have_lead_to_something = {}

    stillTelling = True

    count = 0

    while stillTelling and count < 30:
        count = count + 1
        bound_arguments = None
        narrative_piece = None
        
        pieces = noir.narrative_pieces.copy()
        random.shuffle(pieces)
        for piece in pieces:
            arguments = try_update_with_beat(
                piece, established_ideas, ideas_that_have_lead_to_something
            )
            if arguments is not None:
                narrative_piece = piece
                break
        if narrative_piece is None:
            print("error no next narrative piece found")
            stillTelling = False
        else:
            print(narrative_piece, " - ", arguments)
            for output_concept in narrative_piece.output_concepts:
                if output_concept is story.story_end:
                    stillTelling = False

    for unused_idea in get_ideas_that_have_lead_nowhere(
        established_ideas, ideas_that_have_lead_to_something
    ):
        print("error: unused idea -", unused_idea)
