import itertools
import random

import util
import story

class EstablishedIdea:
    def __init__(self, concept, arguments):
        self.concept = concept
        self.arguments = arguments
        assert len(concept.parameter_types) == len(arguments)
        assert None not in arguments

    def __repr__(self):
        return str(self.concept) + "-" + str(self.arguments)

# is the required concept understood from the given established idea and
# arguments
def is_established_by(parameterized_concept, established_idea, bound_arguments):
    if established_idea.concept is not parameterized_concept.concept:
        return False

    for p, a in zip(parameterized_concept.parameters, established_idea.arguments):
        assert p in bound_arguments
        if bound_arguments.get(p) is not a:
            return False # This established idea has this same concept but for a
                       # different argument that we have already matched from
                       # another concept in this piece
    return True

def get_established_idea(established_ideas, parameterized_concept, bound_args):
    for idea in established_ideas:
        if is_established_by(parameterized_concept, idea, bound_args):
            return idea
    return None

# See if the idea establishes the concept given the arguments. If some more
# arguments need to be added then do so.
#   - mutates args
def try_is_established_and_bind(parameterized_concept, idea, args):
    if idea.concept is not parameterized_concept.concept:
        return False

    for p, a in zip(parameterized_concept.parameters, idea.arguments):
        if p in args:
            if args.get(p) is not a:
                return False
        else:
            args[p] = a

    return True

# Return arguments to parameters in the required concepts if they are
# established by the given ideas combo
def get_bound_args_if_establishes(narrative_piece, ideas_combo):
    bound_arguments = {}

    for parameterized_concept, idea in zip(
        narrative_piece.parameterized_required_concepts, ideas_combo
    ):
        if not try_is_established_and_bind(
            parameterized_concept, idea, bound_arguments
        ):
            # this isn't a good combo of ideas and parameters
            return None

    return bound_arguments

# Return a generator of bound arguments and used_ideas
def get_possible_basis_ideas(narrative_piece, established_ideas):
    def get_randomized_ideas():
        # Randomize so stories with similar beginnings don't always take the
        # same path
        randomized_established_ideas = established_ideas.copy()
        random.shuffle(randomized_established_ideas)
        return randomized_established_ideas

    random_ideas = [get_randomized_ideas() for _ in range(
        len(narrative_piece.parameterized_required_concepts)
    )]

    combos = itertools.product(*random_ideas)

    return (
        (bound_arguments, combo) for bound_arguments, combo in (
            (get_bound_args_if_establishes(narrative_piece, combo), combo)
            for combo in combos
        ) if bound_arguments is not None
    )

def is_prohibited(narrative_piece, established_ideas, arguments):
    for prohibitive_concept_tuple in narrative_piece.parameterized_prohibitive_concept_tuples:
        if all(
            get_established_idea(
                established_ideas, parameterized_prohibitive_concept, arguments
            )
            is not None for parameterized_prohibitive_concept in prohibitive_concept_tuple
        ):
            return True # One of the prohibitive concept tuples is already established
    return False

def get_ideas_that_have_lead_nowhere(established_ideas, ideas_that_have_lead_to_something):
    return (
        idea for idea in established_ideas
            if not idea not in ideas_that_have_lead_to_something
    )

def try_get_output_args(
    narrative_piece, established_ideas, possible_free_args, requirements_bound_args
):
    all_args = requirements_bound_args.copy()
    for param, arg in possible_free_args:
        assert param not in all_args
        all_args[param] = arg

    if is_prohibited(narrative_piece, established_ideas, all_args):
        return None

    output_args = {}
    for output_concept in narrative_piece.parameterized_output_concepts:
        for output_param in output_concept.parameters:
            assert output_param in all_args
            output_args[output_param] = all_args[output_param]

    found_dup = False

    for output_concept in narrative_piece.parameterized_output_concepts:
        if output_concept.concept.is_exclusive and util.has_duplicates(output_args.values()):
            found_dup = True

    if found_dup:
        # We don't allow selecting the same arg twice if the concept is exclusive
        return None

    # We don't want to establish the same idea twice otherwise the story scene will seem
    # superflous and redundant
    if any(is_established_by(parameterized_output_concept, idea, output_args)
            for idea in established_ideas
            for parameterized_output_concept in narrative_piece.parameterized_output_concepts
        ):
        # we have already established this idea so skip to the next possible free args
        return None

    return output_args

class StoryState:
    def __init__(self, free_arguments):
        self.free_arguments = free_arguments # constant
        self.established_ideas = []
        self.used_ideas = [] # ideas that have lead to something

    def can_beat_be_used(self, narrative_piece):
        for requirements_bound_arguments, used_ideas in get_possible_basis_ideas(
            narrative_piece, self.established_ideas
        ):
            # Parameters from requirements are "bound" and parameters from
            # prohibitive and output concepts are "free"
            free_parameters = {}
            for parameterized_concept in itertools.chain(
                narrative_piece.parameterized_output_concepts,
                *narrative_piece.parameterized_prohibitive_concept_tuples
            ):
                for param, p_type in zip(
                    parameterized_concept.parameters,
                    parameterized_concept.concept.parameter_types
                ):
                    if not param in requirements_bound_arguments:
                        if param in free_parameters:
                            # This can happen if the param is used in outputs
                            # more than once. We don't need to add it twice.
                            assert free_parameters[param] is p_type
                        else:
                            # A parameter in output but not in inputs, we need
                            # to choose a free arg for this
                            free_parameters[param] = p_type

            output_args = None

            # This generator goes once if we have 0 free params (with an empty set of args)
            all_free_arg_combos_generator = itertools.product(
                *(
                    [(param, arg) for arg in self.free_arguments[p_type]]
                        for param, p_type in free_parameters.items()
                )
            )

            lazy_possible_output_args = (
                try_get_output_args(
                    narrative_piece,
                    self.established_ideas,
                    possible_free_args,
                    requirements_bound_arguments
                )
                for possible_free_args in all_free_arg_combos_generator
            )

            output_args = next((
                output_args for output_args in lazy_possible_output_args
                    if output_args is not None
            ), None)

            # All possible free arg sets lead to already established ideas so skip
            # this bound arg possiblity
            if output_args is None:
                continue

            new_established_ideas = []

            for parameterized_output_concept in narrative_piece.parameterized_output_concepts:
                output_arguments = []
                for param in parameterized_output_concept.parameters:
                    bound_arg = output_args[param]
                    assert bound_arg is not None
                    output_arguments.append(bound_arg)

                new_established_ideas.append(EstablishedIdea(
                    parameterized_output_concept.concept, output_arguments
                ))

            # Now do the update steps becuase our match was succesful
            self.established_ideas.extend(new_established_ideas)

            self.used_ideas.extend(used_ideas)
            # end update steps

            return new_established_ideas

        return None

    def try_update_with_beat(self, narrative_piece):

        for parameterized_output_concept in narrative_piece.output_concepts:
            if parameterized_output_concept.concept is story.story_end:
                # lazily check if there's at least one that has lead nowhere
                if next(get_ideas_that_have_lead_nowhere(
                    self.established_ideas, self.used_ideas
                ), None) is not None:
                    return None

        ideas_beat_establishes = self.can_beat_be_used(narrative_piece)

        if ideas_beat_establishes is None:
            return None

        return [arg for arg in (idea.arguments for idea in ideas_beat_establishes)]
