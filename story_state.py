import collections
import itertools
import random

import util
import story

def get_randomized_list(l):
    # Randomize so stories with similar beginnings don't always take the
    # same path
    randomized_list = list(l) # make a copy
    random.shuffle(randomized_list)
    return randomized_list

class EstablishedIdea:
    def __init__(self, concept, key_arguments, value_arguments):
        self.concept = concept
        self.key_arguments = key_arguments
        self.value_arguments = value_arguments
        assert isinstance(key_arguments, tuple)
        assert concept.num_key_parameters == len(key_arguments)
        assert None not in key_arguments
        assert isinstance(value_arguments, tuple)
        assert concept.num_value_parameters == len(value_arguments)
        assert None not in value_arguments

    def __repr__(self):
        return str(self.concept) + "-" + str(self.key_arguments) + (
            ":" + str(self.value_arguments)
            if len(self.value_arguments) > 0
            else ""
        )

    def get_key(self):
        return (self.concept, self.key_arguments)

def reify_parameters(concept_args, bound_args):
    res = []
    for arg in concept_args:
        if isinstance(arg, story.Object):
            reified_arg = arg
        else: # arg is a param
            assert arg in bound_args, str(arg) + " not in " + str(bound_args)
            reified_arg = bound_args[arg]
            assert reified_arg is not None
        res.append(reified_arg)

    return tuple(res)

# is the required concept understood from the given established ideas map and
# arguments
def is_established_by(parameterized_concept, ideas, bound_arguments):
    key = (
        parameterized_concept.concept,
        reify_parameters(parameterized_concept.key_arguments, bound_arguments)
    )

    if key not in ideas:
        return False

    idea = ideas.get(key)

    value_arg_pairs = zip(
        reify_parameters(
            parameterized_concept.value_arguments, bound_arguments
        ),
        idea.value_arguments
    )

    for r, a in value_arg_pairs:
        if r is not a:
            return False # This established idea has this same concept and key 
                # arguments but for a different set of value argument that we
                # have already stored from another concept with this key
    return True

# See if the idea establishes the concept given the arguments. If some more
# arguments need to be added then do so.
#   - mutates args
# TODO: is it possible to speed this one up?
def try_is_established_and_bind(parameterized_concept, idea, args):
    if idea.concept is not parameterized_concept.concept:
        return False

    all_concept_arg_pairs = itertools.chain(
        zip(parameterized_concept.key_arguments, idea.key_arguments),
        zip(parameterized_concept.value_arguments, idea.value_arguments)
    )

    for p, idea_arg in all_concept_arg_pairs:
        if isinstance(p, story.Object):
            arg = p
        elif p in args:
            arg = args.get(p)
        else:
            args[p] = idea_arg
            arg = idea_arg
        if arg is not idea_arg:
            return False

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
        filtered_ideas_per_req = collections.defaultdict(list)

        for idea in established_ideas.values():
            for req in parameterized_required_concepts:
                if idea.concept == req.concept:
                    filtered_ideas_per_req[req].append(idea)

        random_ideas = [
            get_randomized_list(filtered_ideas_per_req[req])
            for req in parameterized_required_concepts
        ]

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
    def is_established_by_and_bind_anys(
        parameterized_concept, established_idea, bound_arguments, bound_anys
    ):
        if established_idea.concept is not parameterized_concept.concept:
            return False

        all_param_arg_pairs = itertools.chain(
            zip(parameterized_concept.key_arguments, established_idea.key_arguments),
            zip(parameterized_concept.value_arguments, established_idea.value_arguments)
        )
        for p, a in all_param_arg_pairs:
            if isinstance(p, story.Object):
                concept_arg = p
            elif p in story.anys:
                if p in bound_anys:
                    concept_arg = bound_anys.get(p)
                else:
                    bound_anys[p] = a
                    concept_arg = a
            else:
                assert p in bound_arguments
                concept_arg = bound_arguments.get(p)
            if concept_arg is not a:
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
        ideas = [established_ideas.values() for _ in range(
            len(prohibitive_concept_tuple)
        )]
        combos = itertools.product(*ideas)

        for combo in combos:
            if combo_establishes_prohib_tuple(prohibitive_concept_tuple, combo):
                # One of the prohibitive concept tuples is already established
                return True

    return False

def merge_args(args1, args2, allow_same=False):
    all_args = args1.copy()
    for param, arg in args2.items():
        assert param not in all_args or (arg is all_args[param] and allow_same), (
            str(param) + " duped for " + str(args1) + " " + str(args2)
        )
        all_args[param] = arg
    return all_args

def get_all_parameters(parameterized_concept):
    return (
        arg for arg in itertools.chain(
            parameterized_concept.key_arguments,
            parameterized_concept.value_arguments
        ) if not isinstance(arg, story.Object)
    )

def try_get_output_args(narrative_piece, established_ideas, all_non_output_args):
    if is_prohibited(narrative_piece, established_ideas, all_non_output_args):
        return None

    output_args = {}
    for output_concept in narrative_piece.parameterized_output_concepts:
        for output_param in get_all_parameters(output_concept):
            assert output_param in all_non_output_args
            output_args[output_param] = all_non_output_args[output_param]

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
        is_established_by(
            parameterized_output_concept, established_ideas, output_args
        )
        for parameterized_output_concept in narrative_piece.parameterized_output_concepts
    ):
        # we have already established these ideas so fail for these args
        return None

    return output_args

def get_ideas_that_have_lead_nowhere(established_ideas, used_ideas):
    return (idea for idea in established_ideas if idea not in used_ideas)

class StoryState:
    def __init__(self, content_packs):
        # established_ideas is key->value current state store, common concepts
        # are permanent and have keys but an empty set of values
        self.established_ideas = {}
        self.used_ideas = set() # ideas that have lead to something
        for content_pack in content_packs:
            for parameterized_concept in content_pack.pre_established_concepts:
                self.establish_idea(parameterized_concept, {})
        self.objects = []
        for content_pack in content_packs:
            for obj in content_pack.objects:
                self.objects.append(obj)
        self.object_expressions = {}
        for content_pack in content_packs:
            for obj, expression in content_pack.object_expressions.items():
                assert obj not in self.object_expressions
                self.object_expressions[obj] = expression

    def establish_idea(self, parameterized_concept, args_map):
        key_arguments = reify_parameters(
            parameterized_concept.key_arguments, args_map
        )

        value_arguments = reify_parameters(
            parameterized_concept.value_arguments, args_map
        )

        idea = EstablishedIdea(
            parameterized_concept.concept,
            tuple(key_arguments),
            tuple(value_arguments)
        )

        key = idea.get_key()
        if key in self.established_ideas:
            existing_value = self.established_ideas[key].value_arguments
            if existing_value != idea.value_arguments:
                print("==Replacing", existing_value, "with:", idea, "for next beat==")
        self.established_ideas[key] = idea

    def try_update_with_beat(self, narrative_piece):
        for requirements_bound_arguments, used_ideas in get_possible_basis_ideas(
            narrative_piece, self.established_ideas
        ):
            # Parameters from requirements are "bound" and parameters from
            # prohibitive and output concepts are "free"
            free_parameters = []
            for parameterized_concept in itertools.chain(
                narrative_piece.parameterized_output_concepts,
                *narrative_piece.parameterized_prohibitive_concept_tuples
            ):
                for param in get_all_parameters(parameterized_concept):
                    if param not in requirements_bound_arguments and param not in story.anys:
                        if param in free_parameters:
                            # This can happen if the param is used in outputs
                            # more than once. We don't need to add it twice.
                            pass
                        else:
                            # A parameter in output but not in inputs, we need
                            # to choose a free arg for this
                            free_parameters.append(param)

            output_args = None

            # This generator goes once if we have 0 free params (with an empty set of args)
            all_free_arg_combos_generator = (
                dict(pairs) for pairs in itertools.product(
                    *(
                        [(param, obj) for obj in self.objects]
                            for param in free_parameters
                    )
                )
            )

            output_args = None
            all_args = None
            for possible_free_args in all_free_arg_combos_generator:
                all_non_output_args = merge_args(
                    requirements_bound_arguments, possible_free_args
                )
                output_args = try_get_output_args(
                    narrative_piece,
                    self.established_ideas,
                    all_non_output_args
                )
                if output_args is not None:
                    all_args = merge_args(
                        all_non_output_args, output_args, allow_same=True
                    )
                    break

            # All possible free arg sets lead to already established ideas so skip
            # this bound arg possiblity
            if output_args is None:
                continue

            if not self.can_story_end(narrative_piece, used_ideas):
                continue

            # Now do the update steps becuase our match was succesful
            for parameterized_output_concept in narrative_piece.parameterized_output_concepts:
                self.establish_idea(parameterized_output_concept, output_args)

            self.used_ideas.update(used_ideas)
            # end update steps

            expressions = []

            for expression in narrative_piece.parameterized_expressions:
                expr_args = {}
                for expr_param, arg in expression.parameter_map.items():
                    if isinstance(arg, story.Object):
                        obj = arg
                    else:
                        assert arg in all_args, (
                            "Missing " + str(arg) + " for " + str(expression) +
                            " in " + str(narrative_piece)
                        )
                        obj = all_args[arg]
                    expr_arg = self.object_expressions[obj]
                    expr_args[expr_param] = expr_arg

                reified_expression = story.Expression(
                    expression.core, expr_args, expression.modifiers
                )
                expressions.append(reified_expression)

            return expressions

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
