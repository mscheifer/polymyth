import collections
import itertools

# If we break the narrative down into small enough pieces, it becomes a language. We can recombine
# the pieces to create novelty. Repeating the same building blocks does not sound repetative, just
# like words.

any1 = 'any1'
any2 = 'any2'
any3 = 'any3'

anys = [any1, any2, any3]

class MakeBeat:
    def __init__(self, text):
        self.text = text
        self.required_concept_tuples = []
        self.prohibitive_concept_tuples = []

    # One call to ok_if() creates a set of concepts that must all be present for this beat to be
    # allowed. If you want to allow this beat for any of several concepts, just call ok_if()
    # for each one.
    def ok_if(self, *required_concepts):
        self.required_concept_tuples.append(tuple(required_concepts))
        return self

    # One call to if_not() creates a set of concepts that must all be present for this beat to be
    # prohibited. If you want to prohibit this beat for any of several concepts, just call if_not()
    # for each one.
    def if_not(self, *prohibitive_concepts):
        self.prohibitive_concept_tuples.append(tuple(prohibitive_concepts))
        return self

    def sets_up(self, *output_concepts):
        return NarrativePiece(
            self.text,
            self.required_concept_tuples,
            output_concepts,
            self.prohibitive_concept_tuples
        )

class NarrativePiece:
    def __init__(
        self,
        text,
        required_concept_tuples,
        output_concepts,
        prohibitive_concept_tuples,
    ):
        self.text = text

        self.parameterized_required_concept_tuples = [
            [req.get_parameterized() for req in tup]
            for tup in required_concept_tuples
        ]
        # No set requirements implys that it's always allowed, so we change it
        # to one possible req of nothing.
        if len(self.parameterized_required_concept_tuples) == 0:
            self.parameterized_required_concept_tuples = [[]]

        #TODO: should convert to tuple again here?
        self.parameterized_prohibitive_concept_tuples = [
            [prohib.get_parameterized() for prohib in tup]
            for tup in prohibitive_concept_tuples
        ]
        self.parameterized_output_concepts = [
            out.get_parameterized() for out in output_concepts
        ]

        all_prohib_params = set(param
            for concept in itertools.chain.from_iterable(
                self.parameterized_prohibitive_concept_tuples
            )
            for param in (
                list(concept.key_parameters) + list(concept.value_parameters)
            )
        )

        # Bound params must be used in both prohbited concepts and something
        # else, or they can be one of the specific ANYs.
        for param in all_prohib_params:
            assert (
                any(
                    param in (
                        list(param_output_concept.key_parameters) +
                        list(param_output_concept.value_parameters)
                    )
                    for param_output_concept in self.parameterized_output_concepts
                ) or
                any(
                    param in (
                        list(param_req_concept.key_parameters) +
                        list(param_req_concept.value_parameters)
                    )
                    for param_req_concepts in self.parameterized_required_concept_tuples
                    for param_req_concept in param_req_concepts
                ) or
                param in anys
            ), "Cannot use non-any param: " + str(param) + " only in prohibited concepts"

        all_parameterized_concepts = itertools.chain(
            *self.parameterized_required_concept_tuples,
            self.parameterized_output_concepts,
            *self.parameterized_prohibitive_concept_tuples
        )

        named_param_to_types = collections.defaultdict(set)

        for c in all_parameterized_concepts:
            for param, param_type in itertools.chain(
                zip(c.key_parameters, c.concept.key_parameter_types),
                zip(c.value_parameters, c.concept.value_parameter_types)
            ):
                named_param_to_types[param].add(param_type)

        for named_param, types in named_param_to_types.items():
            assert len(types) == 1, (
                str(named_param) + " used with more than one type:" + str(types)
            )

    def __repr__(self):
        return self.text

class Concept:
    # In the common case, value_parameters is empty, so there is only 1 possible
    # value for the "key", which means it's just a normal concept established
    # once. If there are value parameters then the concept can be re-established
    # with the same key and different values, replacing the previous state.
    #
    # is exclusive is whether two parameters can be bound to the same thing
    def __init__(
        self,
        key_parameter_types,
        debug_name=None,
        value_parameter_types=[],
        is_exclusive=False
    ):
        assert isinstance(key_parameter_types, list)
        assert None not in key_parameter_types
        assert isinstance(value_parameter_types, list)
        assert None not in value_parameter_types
        self.key_parameter_types = key_parameter_types
        self.value_parameter_types = value_parameter_types
        self.debug_name = debug_name
        self.is_exclusive = is_exclusive

    def get_parameterized(self):
        assert len(self.key_parameter_types) == 0, (
             "You must pass in names for the paramters to: " + str(self)
        )
        assert len(self.value_parameter_types) == 0, (
             "You must pass in names for the paramters to: " + str(self)
        )
        return _ParameterizedConcept(self, [], [])

    def __repr__(self):
        if self.debug_name is None:
            return super().__repr__()
        return self.debug_name

    def __call__(self, *args):
        return _ParameterizedConcept(self, args, [])

    # current() is a convience feature to track mutable state that changes over the
    # course of the story. It is possible to do everything this function is used for
    # by manually managing ordered sections of the story as concepts but that
    # approach is verbose and buggy, and likely unnecessarily rigid. For example: if
    # you were tracking the current location of a character you could define like 7
    # points of time and then have every beat check each time and check against the
    # subsequent time. That's already pretty verbose and it restricts how much the
    # character can move. Making it more flexible would make it even more
    # complicated, and you would still have to choose some finite limit.
    def current(self, key_arguments, variable_arguments):
        return _ParameterizedConcept(self, key_arguments, variable_arguments)

class _ParameterizedConcept:
    def __init__(self, concept, key_parameters, value_parameters):
        self.concept = concept
        assert None not in key_parameters
        assert None not in value_parameters
        assert len(key_parameters) == len(concept.key_parameter_types)
        assert len(value_parameters) == len(concept.value_parameter_types)
        self.key_parameters = key_parameters
        self.value_parameters = value_parameters

    def get_parameterized(self):
        return self

    def __repr__(self):
        return "P-" + str(self.concept)


story_end = Concept([], "##END##")
