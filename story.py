class NarrativePiece:
    def __init__(self, text, required_concepts, output_concept, input_to_output_params, linked_parameters=[], is_end=False):
        self.text = text
        self.required_concepts = required_concepts
        self.output_concept = output_concept
        self.input_to_output_params = input_to_output_params
        self.linked_parameters = linked_parameters
        assert iter(linked_parameters)
        for link_set in linked_parameters:
            assert iter(link_set)
        self.is_end = is_end

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

# Parm types
charParam = 'char_param_type'

characterHasDeadBrother = Concept([charParam], "deadBro")
characterIsPI = Concept([charParam], "isPI")

# 1st parameter is the detective
caseOfMissingFather = Concept([charParam], "missingFather")

# 1st parameter is the detective, 2nd is mentor
# The params are exclusive because you can't get advice from yourself.
hasGuidance = Concept([charParam, charParam], "hasGuidance", is_exclusive=True)

# 1st parameter is the detective
inFathersAppartment = Concept([charParam], "inFathersAppartment")
# 1st parameter is the detective
foundDeadFather = Concept([charParam], "foundDeadFather")
# 1st parameter is the detective, 2nd param is the perp
foundEvidenceOfPerp = Concept([charParam, charParam], "foundEvidenceOfPerp")
# 1st parameter is the detective, 2nd param is the perp
isAtHouse = Concept([charParam, charParam], "isAtHouse")
# 1st parameter is the perp
runsAway = Concept([charParam], "runsAway")
# 1st parameter is the perp
chasing = Concept([charParam], "chasing")
# 1st parameter is the perp, 2nd param is the detective
cornered = Concept([charParam, charParam], "cornered")
# 1st parameter is the detective
selfDefenseKillPerp = Concept([charParam], "selfDefenseKillPerp")
# 1st parameter is the detective
closure = Concept([charParam], "closure")

isPerp = Concept([charParam])

isDead = Concept([charParam])
isArrested = Concept([charParam])
isArmed = Concept([charParam], "isArmed")

clientHasClosure = Concept([])

def one_to_one_piece(text, req, output):
    input_to_output_params = dict(zip(req.parameters, output.parameters))
    assert len(input_to_output_params) == 1
    return NarrativePiece(text, [req], output, input_to_output_params)

def link_firsts(concept1, concept2):
    return (concept1, concept2)

narrative_pieces = (
    [
        NarrativePiece("Introduce PI", [], characterIsPI, {}),
        NarrativePiece("Introduce dead brother", [], characterHasDeadBrother, {}),
        one_to_one_piece("Father missing case", characterIsPI, caseOfMissingFather),
    ] +
    ([NarrativePiece("Asks old boss for help", [hasACase], hasGuidance, {hasACase.parameters[0]: hasGuidance.parameters[0]})
        for hasACase in [caseOfMissingFather]
    ]) +
    [
        NarrativePiece("Secretly, the boss did it.", [hasGuidance], isPerp, {hasGuidance.parameters[1]: isPerp.parameters[0]}),
        NarrativePiece("Breaks into father's appartment.", [hasGuidance], inFathersAppartment, {hasGuidance.parameters[0]: inFathersAppartment.parameters[0]}),
        one_to_one_piece("Finds father dead.", inFathersAppartment, foundDeadFather),

        NarrativePiece("Knows now that his old boss did it.", [foundDeadFather, hasGuidance],
            foundEvidenceOfPerp, dict(zip(hasGuidance.parameters, foundEvidenceOfPerp.parameters)),
            [link_firsts(foundDeadFather, hasGuidance)]),

        NarrativePiece("Goes to his old bosses place.", [foundEvidenceOfPerp], isAtHouse,
            dict(zip(foundEvidenceOfPerp.parameters, isAtHouse.parameters))),

        NarrativePiece("Boss sees PI and bolts.", [isAtHouse, isPerp], runsAway,
            {isPerp.parameters[0]: runsAway.parameters[0]}, [(isAtHouse.parameters[1], isPerp.parameters[0])]),

        one_to_one_piece("PI chases old boss.", runsAway, chasing),

        NarrativePiece("Old boss gets cornered down an alley.", [chasing], cornered, {chasing.parameters[0]: cornered.parameters[0]}),
        NarrativePiece("Old boss pulls a gun. Fires on our hero and misses. PI kills old boss.",
            [cornered, isArmed], isDead, {isArmed.parameters[0]: isDead.parameters[0]},
            [link_firsts(cornered, isArmed)])
    ] +
    ([NarrativePiece("Client learns who kidnapped/killed father and thanks PI for closure",
            [isPerp, perpResolved], clientHasClosure, {}, [link_firsts(isPerp, perpResolved)], is_end=True)
        for perpResolved in [isDead, isArrested]
    ])
)

free_characters = frozenset(["Alan", "Sarah", "David", "Julie"])

# TODO: add other non-character params to this map with their own argument sets
free_arguments = {charParam:free_characters}
