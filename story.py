import collections
import itertools

import util

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

        all_named_param_concepts = itertools.chain(
            required_concepts, output_concepts, *prohibitive_concept_tuples
        )

        reqs_names_to_params = collections.defaultdict(set)

        for concept in all_named_param_concepts:
            for name, arg in concept.get_named_params():
                reqs_names_to_params[name].add(arg)

        linked_parameters = []

        for args in reqs_names_to_params.values():
            linked_parameters.append(args)

        self.required_concepts = [req.get_concept() for req in required_concepts]
        self.prohibitive_concept_tuples = [
            [req.get_concept() for req in prohibitive_concepts]
            for prohibitive_concepts in prohibitive_concept_tuples
        ]
        self.output_concepts = [req.get_concept() for req in output_concepts]
        self.linked_parameters = linked_parameters

        # Because we are storing linked parameters as big sets, it won't support multiple of
        # the same concept right now
        assert not util.has_duplicates(list(itertools.chain(
            self.required_concepts,
            *self.prohibitive_concept_tuples,
            self.output_concepts,
        )))

        assert iter(linked_parameters)
        for link_set in linked_parameters:
            assert iter(link_set)

    def __repr__(self):
        return self.text

class Parameter:
    def __init__(self, p_type):
        self.p_type = p_type

    def __repr__(self):
        return "P" + self.p_type

class Concept:
    # is exclusive is whether two parameters can be bound to the same thing
    def __init__(self, parameter_types, debug_name=None, is_exclusive=False):
        assert isinstance(parameter_types, list)
        assert None not in parameter_types
        self.parameters = [Parameter(p_type) for p_type in parameter_types]
        self.debug_name = debug_name
        self.is_exclusive = is_exclusive

    def __repr__(self):
        if self.debug_name is None:
            return super().__repr__()
        return self.debug_name

    def __call__(self, *args):
        return ConceptWithNamedArgs(self, args)

    def get_named_params(self):
        return []

    def get_concept(self):
        return self

class ConceptWithNamedArgs:
    def __init__(self, concept, args):
        self.concept = concept
        self.names_to_params = zip(args, concept.parameters)

    def get_concept(self):
        return self.concept

    def get_named_params(self):
        return self.names_to_params

def one_to_one_piece(text, req, output):
    assert len(req.parameters) == 1
    assert len(output.parameters) == 1
    return NarrativePiece(text, [req(1)], output(1))

#TODO: can keep large sections under one concept (like prose style) as a nested constructor thing

story_end = Concept([])
