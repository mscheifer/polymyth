from story import Concept, NarrativePiece, one_to_one_piece, story_end

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
# 1st parameter is the perp, 2nd param is the detective
chasing = Concept([charParam, charParam], "chasing")
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

isObsessive = Concept([charParam])

narrative_pieces = (
    [
        NarrativePiece("Introduce PI", [], characterIsPI),
        NarrativePiece("Introduce dead brother", [], characterHasDeadBrother),
        one_to_one_piece("Father missing case", characterIsPI, caseOfMissingFather),
    ] +
    ([NarrativePiece("Asks old boss for help", [hasACase(1)], hasGuidance(1))
        for hasACase in [caseOfMissingFather]
    ]) +
    [
        NarrativePiece("Secretly, the boss did it.", [hasGuidance(0,1)], isPerp(1)),
        NarrativePiece("Breaks into father's appartment.", [hasGuidance(1)], inFathersAppartment(1)),
        one_to_one_piece("Finds father dead.", inFathersAppartment, foundDeadFather),

        NarrativePiece("Knows now that his old boss did it.", [foundDeadFather(1), hasGuidance(1,2)],
            foundEvidenceOfPerp(1,2)),

        NarrativePiece("Goes to his old bosses place.", [foundEvidenceOfPerp(1,2)], isAtHouse(1,2)),

        NarrativePiece("Boss sees PI and bolts.", [isAtHouse(0,1), isPerp(1)], runsAway(1)),

        NarrativePiece("PI chases old boss.", [runsAway(1)], chasing(1)),

        NarrativePiece("Frog 1 is here and I'm going to get him..", [chasing(1), isObsessive(1)],
            story_end),

        NarrativePiece("Old boss gets cornered down an alley.", [chasing(1,2)], cornered(1,2)),
        NarrativePiece("Old boss pulls a gun. Fires on our hero and misses. PI kills old boss.",
            [cornered(1), isArmed(1)], isDead(1))
    ] +
    ([NarrativePiece("Client learns who kidnapped/killed father and thanks PI for closure",
            [isPerp(1), perpResolved(1)], story_end)
        for perpResolved in [isDead, isArrested]
    ])
)

#TODO: concept, children's story logic.

#TODO: if farther from home -> sparser homes. Pavement is cracked up

discreteToContinuous = Concept([], "discrete")
knowPerpIsInChinatown = Concept([], "knowIsInChinatown")

to_add_later = (
    [
        NarrativePiece("You should first describe my life by how I overcame a youthful obsession " +
            "with discrete mathematics and found love with continuous values. Real beauty exists " +
            "again within itself and does not stop at some arbitrary depth.", [], discreteToContinuous),
        NarrativePiece("Forget it Jake, it's Chinatown.", [knowPerpIsInChinatown], story_end),
    ]
)

free_characters = frozenset(["Alan", "Sarah", "David", "Julie"])

# TODO: add other non-character params to this map with their own argument sets
free_arguments = {charParam:free_characters}

#TODO: could make some concepts need to be used more than once to reach an end.

#TODO: generally -> character may do thing in scene because of trait -> characters doing actions can
# create a theme. Setting for action can be caused by another theme.
# farther from starting point (theme) -> road is broken up and overgrown (description).
# rocky road, character has no brains (both description) -> character falls into pot hole (action)
# character fallen down (description) -> dorthy helps them up (action)
# dorthy helps people (deescription) -> thematic conclusion where she is rewarded (theme)
