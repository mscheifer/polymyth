import itertools
import random

import util
import story

def get_randomized_list(l):
    # Randomize so stories with similar beginnings don't always take the
    # same path
    randomized_list = l.copy()
    random.shuffle(randomized_list)
    return randomized_list

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
def get_bound_args_if_establishes(parameterized_required_concepts, ideas_combo):
    bound_arguments = {}

    for parameterized_concept, idea in zip(
        parameterized_required_concepts, ideas_combo
    ):
        if not try_is_established_and_bind(
            parameterized_concept, idea, bound_arguments
        ):
            # this isn't a good combo of ideas and parameters
            return None

    return bound_arguments

# Return a generator of bound arguments and used_ideas
def get_possible_basis_ideas(narrative_piece, established_ideas):
    # Each possible set of required concepts will become an iterator of all
    # establishing ideas for those concepts.

    def get_combo_iterator(parameterized_required_concepts):
        random_ideas = [get_randomized_list(established_ideas) for _ in range(
            len(parameterized_required_concepts)
        )]

        combos = itertools.product(*random_ideas)

        def maybe_get_bound_args(combo):
            return get_bound_args_if_establishes(
                parameterized_required_concepts, combo
            )

        return (
            (bound_arguments, combo) for bound_arguments, combo in (
                (maybe_get_bound_args(combo), combo) for combo in combos
            ) if bound_arguments is not None
        )

    combo_iterators = (get_combo_iterator(tup)
        # Randomize so we don't always bind to args in the first possiblility
        # when they work. If all requirements could work then we should pick
        # with equal probability.
        for tup in get_randomized_list(
            narrative_piece.parameterized_required_concept_tuples
        ))

    return itertools.chain.from_iterable(combo_iterators)

def is_prohibited(narrative_piece, established_ideas, arguments):
    def is_established_by_and_bind_anys(parameterized_concept, established_idea, bound_arguments, bound_anys):
        if established_idea.concept is not parameterized_concept.concept:
            return False

        for p, a in zip(parameterized_concept.parameters, established_idea.arguments):
            if p in story.anys:
                if p in bound_anys:
                    if bound_anys.get(p) is not a:
                        return False
                else:
                    bound_anys[p] = a
            else:
                assert p in bound_arguments
                if bound_arguments.get(p) is not a:
                    return False

        return True

    def combo_establishes_prohib_tuple(prohibitive_concept_tuple, combo):
        bound_anys = {}
        for concept, idea in zip(prohibitive_concept_tuple, combo):
            if not is_established_by_and_bind_anys(
                concept, idea, arguments, bound_anys
            ):
                return False
        return True

    for prohibitive_concept_tuple in (
        narrative_piece.parameterized_prohibitive_concept_tuples
    ):
        ideas = [established_ideas for _ in range(
            len(prohibitive_concept_tuple)
        )]
        combos = itertools.product(*ideas)

        for combo in combos:
            if combo_establishes_prohib_tuple(prohibitive_concept_tuple, combo):
                # One of the prohibitive concept tuples is already established
                return True

    return False

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

    # We don't want to establish the same ideas twice otherwise the story beat
    # will seem superflous. This functionality is redundant with prohibited
    # concepts but we would want this on every beat so it is added here for
    # convienence.
    if all(
        any(
            is_established_by(parameterized_output_concept, idea, output_args)
            for idea in established_ideas
        )
        for parameterized_output_concept in narrative_piece.parameterized_output_concepts
    ):
        # we have already established these ideas so fail for these args
        return None

    return output_args

def get_ideas_that_have_lead_nowhere(established_ideas, used_ideas):
    return (idea for idea in established_ideas if idea not in used_ideas)

class StoryState:
    def __init__(self, free_arguments):
        self.free_arguments = free_arguments # constant
        self.established_ideas = []
        self.used_ideas = set() # ideas that have lead to something

    def try_update_with_beat(self, narrative_piece):
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
                    if param not in requirements_bound_arguments and param not in story.anys:
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

            if not self.can_story_end(narrative_piece, used_ideas):
                continue

            # Now do the update steps becuase our match was succesful

            for parameterized_output_concept in narrative_piece.parameterized_output_concepts:
                output_arguments = []
                for param in parameterized_output_concept.parameters:
                    bound_arg = output_args[param]
                    assert bound_arg is not None
                    output_arguments.append(bound_arg)

                self.established_ideas.append(EstablishedIdea(
                    parameterized_output_concept.concept, output_arguments
                ))

            self.used_ideas.update(used_ideas)
            # end update steps

            return output_args, used_ideas

        return None

    def can_story_end(self, narrative_piece, new_used_ideas):
        for parameterized_concept in narrative_piece.parameterized_output_concepts:
            if parameterized_concept.concept is story.story_end:
                # lazily check if there's at least one that has lead nowhere
                used_ideas = set.union(self.used_ideas, set(new_used_ideas))
                if next(get_ideas_that_have_lead_nowhere(
                    self.established_ideas, used_ideas
                ), None) is not None:
                    return False
        return True
