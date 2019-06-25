from story import (
    Concept,
    NarrativePiece,
    MakeBeat,
    one_to_one_piece,
    story_end
)
import heros_journey

# Parm types
charParam = 'char_param_type'

characterHasDeadBrother = Concept([charParam], "deadBro")
characterIsPI = Concept([charParam], "isPI")

# 1st parameter is the detective
hasACase = Concept([charParam], "hasACase")
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

storyStart = Concept([], "##start##")

isProtag = Concept([charParam], "isProtag")
isPerp = Concept([charParam], "isPerp")
isClient = Concept([charParam], "isClient")

isInPIOffice = Concept([charParam], "isInPIOffice")
isDead = Concept([charParam], "isDead")
isArrested = Concept([charParam], "isArrested")
isArmed = Concept([charParam], "isArmed")

isObsessive = Concept([charParam], "isObessive")

wifeDiedRandomly = Concept([charParam], "wifeDiedRandomly")
regainFaith = Concept([charParam], "regainFaith")

politicalScandal = Concept([], "politicalScandal")

narrative_pieces = (
    [
        MakeBeat("Introduce PI")
            .if_not(storyStart) # any
            .sets_up(storyStart, characterIsPI(1), isInPIOffice(1)),
        MakeBeat("PI is protagonist")
            .needs(characterIsPI(1))
            .if_not(isProtag) # any
            .sets_up(isProtag(1)),

        MakeBeat("Reads political scandal in paper")
            .needs(isInPIOffice)
            .sets_up(politicalScandal),

        MakeBeat("Introduce dead brother")
            .if_not(characterHasDeadBrother)
            .if_not(heros_journey.ghost)
            .sets_up(characterHasDeadBrother, heros_journey.you, heros_journey.ghost),
        MakeBeat("Client walks in")
            .if_not(isInPIOffice(-1), isClient(-1)) # for any other char
            .needs(characterIsPI(0), isInPIOffice(0))
            .sets_up(isInPIOffice(1), isClient(1)),
        MakeBeat("Father missing case")
            .needs(characterIsPI(0), isInPIOffice(1), isClient(1))
            .if_not(hasACase) #Any
            .sets_up(hasACase(0), caseOfMissingFather(0), heros_journey.need),
    ] +
    ([MakeBeat("Asks old boss for help")
        .needs(hasACase(1))
        .if_not(isProtag(2))
        .sets_up(hasGuidance(1, 2))

        for hasACase in [caseOfMissingFather]
    ]) +
    [
        MakeBeat("Breaks into father's appartment.")
            .needs(hasGuidance(1))
            .sets_up(inFathersAppartment(1)),

        MakeBeat("Finds father dead.")
            .needs(inFathersAppartment)
            .sets_up(foundDeadFather, heros_journey.go),

        #TODO(act 2)

        MakeBeat("Finds evidence his old boss did it.")
            .needs(foundDeadFather(1), hasGuidance(1,2))
            .sets_up(foundEvidenceOfPerp(1,2), isPerp(2)),

        MakeBeat("Goes to his old bosses place.")
            .needs(foundEvidenceOfPerp(1,2))
            .sets_up(isAtHouse(1,2)),

        MakeBeat("Boss sees PI and bolts.")
            .needs(isAtHouse(0,1), isPerp(1))
            .sets_up(runsAway(1)),

        MakeBeat("PI chases old boss.").needs(runsAway(1)).sets_up(chasing(1)),

        MakeBeat("Frog 1 is here and I'm going to get him..")
            .needs(chasing(1), isObsessive(1))
            .sets_up(story_end),

        MakeBeat("Old boss gets cornered down an alley.")
            .needs(chasing(1,2))
            .sets_up(cornered(1,2)),

        MakeBeat("Old boss pulls a gun. Fires on our hero and misses. PI kills old boss.")
            .needs(cornered(1), isArmed(1))
            .sets_up(isDead(1))
    ] +
    ([MakeBeat("Client learns who kidnapped/killed father and thanks PI for closure")
            .needs(isPerp(1), perpResolved(1))
            .sets_up(story_end)
        for perpResolved in [isDead, isArrested]
    ] +
    [
        MakeBeat("Wife died suddenly. Her last words didn't mean anything.")
            .if_not(wifeDiedRandomly)
            .if_not(heros_journey.ghost)
            .sets_up(wifeDiedRandomly, heros_journey.ghost),
        MakeBeat("Wife last words become meaningful.")
            .needs(wifeDiedRandomly(1), heros_journey.theReturn)
            .sets_up(regainFaith(1), heros_journey.change),
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
            "again within itself and does not stop at some arbitrary depth.", [], [discreteToContinuous], []),
        NarrativePiece("Forget it Jake, it's Chinatown.", [knowPerpIsInChinatown], [story_end], []),
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
