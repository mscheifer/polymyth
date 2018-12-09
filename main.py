import itertools
import story

class EstablishedIdea:
    def __init__(self, concept, arguments):
        self.concept = concept
        self.arguments = arguments
        assert len(concept.parameters) == len(arguments) 
        assert None not in arguments

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
    if narrative_piece.is_end:
        for idea in established_ideas:
            if not ideas_that_have_lead_to_something.get(idea, False):
                # We can't end the story yet because not all ideas have lead to something
                return None
    bound_arguments = {}
    used_ideas = []
    for concept in narrative_piece.required_concepts:
        # lazily find the first idea that this concept is established by
        idea = next(
            (idea for idea in established_ideas if is_established_by(
                concept, idea, bound_arguments
            )),
            None
        )
        if idea is None:
            return None # we didn't find an idea to match this concept
        for p_a in zip(concept.parameters, idea.arguments):
            assert p_a[0] not in bound_arguments or bound_arguments[p_a[0]] is p_a[1]
            bound_arguments[p_a[0]] = p_a[1]
        used_ideas.append(idea)

    free_parameters = []
    for param in narrative_piece.output_concept.parameters:
        if not param in bound_arguments:
            # A parameter in output but not in inputs, we need to choose a free arg for this but
            # only if the resulting output concept is not already established.
            free_parameters.append(param)

    bound_and_free_args = None

    all_free_arg_combos_generator = (itertools.product(
        *(story.free_arguments[param] for param in free_parameters))
    )

    # TODO: make sure this loop goes at least once if we have 0 free params
    for possible_free_args in all_free_arg_combos_generator:

        bound_and_free_args = bound_arguments.copy()
        for param, arg in zip(free_parameters, possible_free_args):
            bound_and_free_args[param] = arg

        # We don't want to establish the same idea twice otherwise the story scene will seem
        # superflous and redundant
        if any(is_established_by(
                narrative_piece.output_concept, idea, bound_and_free_args) for idea in established_ideas
            ):
            # we have already established this idea so skip to the next possible free args
            bound_and_free_args = None
        else:
            break # we can establish a new idea with these free args

    # All possible free arg sets lead to already established ideas so skip this piece
    if bound_and_free_args is None:
        return None

    output_arguments = [] 
    for param in narrative_piece.output_concept.parameters:
        bound_arg = bound_and_free_args[param]
        assert bound_arg is not None
        output_arguments.append(bound_arg)

    established_idea = EstablishedIdea(narrative_piece.output_concept, output_arguments)

    # Now do the update steps becuase our match was succesful
    established_ideas.append(established_idea)

    for idea in used_ideas:
        ideas_that_have_lead_to_something[idea] = True

    return bound_and_free_args

established_ideas = []
ideas_that_have_lead_to_something = {}

stillTelling = True

while stillTelling:
    bound_arguments = None
    narrative_piece = None
    for piece in story.narrative_pieces:
        arguments = tryBindAndUpdate(piece, established_ideas, ideas_that_have_lead_to_something)
        if arguments is not None:
            narrative_piece = piece
            break
    if narrative_piece is None:
        print("error no next narrative piece found")
        stillTelling = False
    else:
        print(narrative_piece, " - ", arguments)
        if narrative_piece.is_end:
            stillTelling = False
