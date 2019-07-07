# If we break the narrative down into small enough pieces, it becomes a language. We can recombine
# the pieces to create novelty. Repeating the same building blocks does not sound repetative, just
# like words.

class MakeBeat:
    def __init__(self, text):
        self.text = text
        self.required_concepts = []
        self.prohibitive_concept_tuples = []

    #TODO rename to 'ok_if' and have each call be OR'd (top level) and arguments are ANDed
    def needs(self, *required_concepts):
        self.required_concepts = required_concepts
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
            self.required_concepts,
            output_concepts,
            self.prohibitive_concept_tuples
        )

class NarrativePiece:
    def __init__(
        self,
        text,
        required_concepts,
        output_concepts,
        prohibitive_concept_tuples,
    ):
        self.text = text

        self.parameterized_required_concepts = [
            req.get_parameterized() for req in required_concepts
        ]
        self.parameterized_prohibitive_concept_tuples = [
            [prohib.get_parameterized() for prohib in tup]
            for tup in prohibitive_concept_tuples
        ]
        self.parameterized_output_concepts = [
            out.get_parameterized() for out in output_concepts
        ]

    def __repr__(self):
        return self.text

class Concept:
    # is exclusive is whether two parameters can be bound to the same thing
    def __init__(self, parameter_types, debug_name=None, is_exclusive=False):
        assert isinstance(parameter_types, list)
        assert None not in parameter_types
        self.parameter_types = parameter_types
        self.debug_name = debug_name
        self.is_exclusive = is_exclusive

    def get_parameterized(self):
        assert len(self.parameter_types) == 0, (
             "You must pass in names for the paramters to: " + self
        )
        return self()

    def __repr__(self):
        if self.debug_name is None:
            return super().__repr__()
        return self.debug_name

    def __call__(self, *args):
        return _ParameterizedConcept(self, args)

class _ParameterizedConcept:
    def __init__(self, concept, parameters):
        self.concept = concept
        assert len(parameters) == len(concept.parameter_types)
        self.parameters = parameters

    def get_parameterized(self):
        return self

    def __repr__(self):
        return "P-" + self.concept

story_end = Concept([])
