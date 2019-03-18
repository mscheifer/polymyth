import collections

# If we break the narrative down into small enough pieces, it becomes a language. We can recombine
# the pieces to create novelty. Repeating the same building blocks does not sound repetative, just
# like words.

class NarrativePiece:
    def __init__(self, text, required_concepts, output_concept):

        reqs_names_to_params = collections.defaultdict(list)

        for concept in required_concepts:
            for name, arg in concept.get_named_params():
                reqs_names_to_params[name].append(arg)

        linked_parameters = []

        for args in reqs_names_to_params.values():
            linked_parameters.append(args)

        input_to_output_params = {}

        for name, arg in output_concept.get_named_params():
            for param in reqs_names_to_params[name]:
                input_to_output_params[param] = arg

        self.text = text
        self.required_concepts = [req.get_concept() for req in required_concepts]
        self.output_concept = output_concept.get_concept()
        self.input_to_output_params = input_to_output_params
        self.linked_parameters = linked_parameters
        assert iter(linked_parameters)
        for link_set in linked_parameters:
            assert iter(link_set)

    def __str__(self):
        return self.text

class Parameter:
    def __init__(self, p_type):
        self.p_type = p_type

class Concept:
    # is exclusive is whether two parameters can be bound to the same thing
    def __init__(self, parameter_types, debug_name=None, is_exclusive=False):
        assert None not in parameter_types
        self.parameters = [Parameter(p_type) for p_type in parameter_types]
        self.debug_name = debug_name
        self.is_exclusive = is_exclusive

    def __str__(self):
        if self.debug_name is None:
            return super().__str__()
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
