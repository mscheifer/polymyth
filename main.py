import itertools
import story
import noir

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

def get_linked_bound_args(narrative_piece, concept, bound_arguments):
    linked_bound_args = {}
    for parameter in concept.parameters:
        for link_set in narrative_piece.linked_parameters:
            if parameter in link_set:
                for other_param in link_set:
                    if other_param in bound_arguments:
                        existing_val = linked_bound_args.get(parameter)
                        assert existing_val is None or exisiting_val is bound_args[other_param]
                        linked_bound_args[parameter] = bound_arguments[other_param]

    return linked_bound_args


# is the required concept understood from the given established idea and arguments we have bound
# from other understood concepts
def is_established_by(concept, established_idea, bound_arguments):
    if established_idea.concept is not concept:
        return False

    for p_a in zip(concept.parameters, established_idea.arguments):
        if p_a[0] in bound_arguments and bound_arguments.get(p_a[0]) is not p_a[1]:
            return False # This established idea has this same concept but for a
                       # different argument that we have already matched from
                       # another concept in this piece
    return True

def tryBindAndUpdate(narrative_piece, established_ideas, ideas_that_have_lead_to_something):
    if narrative_piece.output_concept is story.story_end:
        for idea in established_ideas:
            if not ideas_that_have_lead_to_something.get(idea, False):
                # We can't end the story yet because not all ideas have lead to something
                return None
    bound_arguments = {}
    used_ideas = []
    for concept in narrative_piece.required_concepts:
        linked_bound_args = get_linked_bound_args(narrative_piece, concept, bound_arguments)
        # lazily find the first idea that this concept is established by
        idea = next(
            (idea for idea in established_ideas if is_established_by(
                concept, idea, linked_bound_args
            )),
            None
        )
        if idea is None:
            return None # we didn't find an idea to match this concept
        for p_a in zip(concept.parameters, idea.arguments):
            assert p_a[0] not in bound_arguments
            bound_arguments[p_a[0]] = p_a[1]
        used_ideas.append(idea)

    # TODO: need to use linked prohibitive concepts to skip establishment

    #TODO: if the bound arguments we picked didn't work out, we need to look for other established
    # ideas that would lead to different bindings

    output_bound_args = {}
    for param, arg in bound_arguments.items():
        if param in narrative_piece.input_to_output_params:
            output_bound_args[narrative_piece.input_to_output_params[param]] = arg

    free_parameters = []
    for param in narrative_piece.output_concept.parameters:
        if not param in output_bound_args:
            # A parameter in output but not in inputs, we need to choose a free arg for this but
            # only if the resulting output concept is not already established.
            free_parameters.append(param)

    output_args = None

    all_free_arg_combos_generator = (itertools.product(
        *(noir.free_arguments[param.p_type] for param in free_parameters))
    )

    # This loop goes once if we have 0 free params
    for possible_free_args in all_free_arg_combos_generator:

        output_args = output_bound_args.copy()

        for param, arg in zip(free_parameters, possible_free_args):
            output_args[param] = arg

        if narrative_piece.output_concept.is_exclusive and has_duplicates(output_args.values()):
            # We don't allow selecting the same arg twice if the concept is exclusive
            output_args = None
            continue

        # We don't want to establish the same idea twice otherwise the story scene will seem
        # superflous and redundant
        if any(is_established_by(
                narrative_piece.output_concept, idea, output_args) for idea in established_ideas
            ):
            # we have already established this idea so skip to the next possible free args
            output_args = None
        else:
            break # we can establish a new idea with these free args

    # All possible free arg sets lead to already established ideas so skip this piece
    if output_args is None:
        #TODO: in this case I actually need to try the whole thing again with different params from
        # different established ideas
        return None

    output_arguments = [] 
    for param in narrative_piece.output_concept.parameters:
        bound_arg = output_args[param]
        assert bound_arg is not None
        output_arguments.append(bound_arg)

    established_idea = EstablishedIdea(narrative_piece.output_concept, output_arguments)

    # Now do the update steps becuase our match was succesful
    established_ideas.append(established_idea)

    for idea in used_ideas:
        ideas_that_have_lead_to_something[idea] = True

    return output_arguments

established_ideas = []
ideas_that_have_lead_to_something = {}

stillTelling = True

count = 0

while stillTelling and count < 30:
    count = count + 1
    bound_arguments = None
    narrative_piece = None
    for piece in noir.narrative_pieces:
        arguments = tryBindAndUpdate(piece, established_ideas, ideas_that_have_lead_to_something)
        if arguments is not None:
            narrative_piece = piece
            break
    if narrative_piece is None:
        print("error no next narrative piece found")
        stillTelling = False
    else:
        print(narrative_piece, " - ", arguments)
        if narrative_piece.output_concept is story.story_end:
            stillTelling = False
