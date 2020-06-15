import collections
import itertools

# If we break the narrative down into small enough pieces, it becomes a language. We can recombine
# the pieces to create novelty. Repeating the same building blocks does not sound repetative, just
# like words.

any1 = 'any1'
any2 = 'any2'
any3 = 'any3'

anys = [any1, any2, any3]

Expression = collections.namedtuple(
    'Expression', 'core argument_map modifiers'
)

class Object:
    def __init__(self, debug_name=None):
        self.debug_name = debug_name if debug_name is not None else "some_object"

    def __repr__(self):
        return "Obj(" + self.debug_name + ")"

# Convert all parameters to strings so it's easier to compare them with
# references in output text format strings
def param_to_string(arg):
    if isinstance(arg, Object):
        return arg
    return str(arg) # if it's not an object, it must be a parameter

class ParameterizedExpression:
    def __init__(self, core, parameter_map, modifiers):
        self.core = core
        self.parameter_map = {
            expr_param : param_to_string(arg)
            for expr_param, arg in parameter_map.items()
        }
        self.modifiers = modifiers

    def __repr__(self):
        return str((self.core, self.parameter_map, self.modifiers))

class MakeBeat:
    def __init__(self, debug_text):
        self.debug_text = debug_text
        self.required_concept_tuples = []
        self.prohibitive_concept_tuples = []
        self.expressions = []

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

    def express(self, expression, parameter_map, *modifiers):
        assert expression.parameters == tuple(parameter_map.keys()), (
            str(expression) + " doesn't match " + str(parameter_map)
        )
        self.expressions.append(
            ParameterizedExpression(expression, parameter_map, modifiers)
        )
        return self

    def sets_up(self, *output_concepts):
        return NarrativePiece(
            self.debug_text,
            self.required_concept_tuples,
            output_concepts,
            self.prohibitive_concept_tuples,
            self.expressions
        )

class NarrativePiece:
    def __init__(
        self,
        debug_text,
        required_concept_tuples,
        output_concepts,
        prohibitive_concept_tuples,
        parameterized_expressions,
    ):
        self.debug_text = debug_text

        self.parameterized_expressions = parameterized_expressions

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

        all_prohib_params = set(argument
            for concept in itertools.chain.from_iterable(
                self.parameterized_prohibitive_concept_tuples
            )
            for argument in (
                list(concept.key_arguments) + list(concept.value_arguments)
            )
            # If it's not a concrete object it must be an object parameter
            if not isinstance(argument, Object)
        )

        # Bound params must in prohbited concepts must also be used in outputs
        # or required concepts, or they can be one of the specific ANYs. The
        # only way a prohibited only param makes sense is with ANY semantics.
        for param in all_prohib_params:
            assert (
                any(
                    param in (
                        list(param_output_concept.key_arguments) +
                        list(param_output_concept.value_arguments)
                    )
                    for param_output_concept in self.parameterized_output_concepts
                ) or
                any(
                    param in (
                        list(param_req_concept.key_arguments) +
                        list(param_req_concept.value_arguments)
                    )
                    for param_req_concepts in self.parameterized_required_concept_tuples
                    for param_req_concept in param_req_concepts
                ) or
                param in anys
            ), "Cannot use non-any param: " + str(param) + " only in prohibited concepts"

    def __repr__(self):
        return self.debug_text

class Concept:
    # In the common case, num_value_parameters is 0, so there is only 1 possible
    # value for the "key", which means it's just a normal concept established
    # once. If there are value parameters then the concept can be re-established
    # with the same key and different values, replacing the previous state.
    def __init__(
        self,
        num_key_parameters,
        debug_name=None,
        num_value_parameters=0
    ):
        self.num_key_parameters = num_key_parameters
        self.num_value_parameters = num_value_parameters
        self.debug_name = debug_name

    def get_parameterized(self):
        assert self.num_key_parameters == 0, (
             "You must pass in symbols for the " + str(self.num_key_parameters)
             + " paramters to: " + str(self)
        )
        assert self.num_value_parameters == 0, (
             "You must pass in symbols for the " +
             str(self.num_value_parameters) + " paramters to: " + str(self)
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
    def __init__(self, concept, key_arguments, value_arguments):
        self.concept = concept
        assert None not in key_arguments
        assert None not in value_arguments
        assert len(key_arguments) == concept.num_key_parameters
        assert len(value_arguments) == concept.num_value_parameters
        self.key_arguments = tuple(param_to_string(p) for p in key_arguments)
        self.value_arguments = tuple(
            param_to_string(p) for p in value_arguments
        )

    def get_parameterized(self):
        return self

    def __repr__(self):
        return "P-" + str(self.concept)

ContentPack = collections.namedtuple(
    'ContentPack',
    'objects pre_established_concepts possible_beats, object_expressions'
)

# This special concept is implemented in the engine. are_different is always
# established if it's two parameters are different.
are_different = Concept(2, "ARE DIFFERENT")

story_end = Concept(0, "##END##")
