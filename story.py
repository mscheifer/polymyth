class NarrativePiece:
    def __init__(self, required_concepts, output_concept, text, is_end=False):
        self.required_concepts = required_concepts
        self.output_concept = output_concept
        self.text = text
        self.is_end = is_end

    def __str__(self):
        return self.text

class Concept:
    def __init__(self, parameters):
        self.parameters = parameters
        assert None not in parameters

charParam = '$char1'
charParam2 = '$char2'
charParam3 = '$char3'
charParams = [charParam, charParam2, charParam3]

characterHasDeadBrother = Concept([charParam])
characterIsPI = Concept([charParam])

caseOfMissingFather = Concept([])

hasACase = {param:Concept([param]) for param in charParams}
hasGuidance = {param:Concept([param]) for param in charParams}

isPerpetrator = {param:Concept([param]) for param in charParams}

# I could just make subconcepts using parameters, but then could I make pieces that depend on a
# specific arg for that parameter?
# Nah, that's weird for union concepts like the resolved as perp

#TODO: isResolvedAsPerpetrator is isDead or isArrested
isResolvedAsPerpetrator = {param:Concept([param]) for param in charParams}

clientHasClosure = Concept([])

narrative_pieces = [
    NarrativePiece([], characterIsPI, "Introduce PI"),
    NarrativePiece([], characterHasDeadBrother, "Introduce dead brother"),
    NarrativePiece([characterIsPI], caseOfMissingFather, "Father missing case"),
    NarrativePiece([hasACase[charParam]], hasGuidance[charParam],
        "Character asks their mentor for help"),
    NarrativePiece([isPerpetrator[charParam], isResolvedAsPerpetrator[charParam]], clientHasClosure,
        "Client learns who kidnapped/killed father and thanks PI for closure"),
]

free_characters = frozenset(["Alan", "Sarah", "David", "Julie"])

# TODO: add other non-character params to this map with their own argument sets
free_arguments = {charParam:free_characters for charParam in charParams}
