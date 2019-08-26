from story import (
    any1,
    Concept,
    NarrativePiece,
    MakeBeat,
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
foundEvidenceOfPerp = Concept([charParam, charParam], "foundEvidenceOfPerp", is_exclusive=True)
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
isCreepy = Concept([charParam], "isCreepy")
isPerp = Concept([charParam], "isPerp")
isClient = Concept([charParam], "isClient")

protagGotShot = Concept([], "protagGotShot")

isHome = Concept([charParam], "isHome")
isInPIOffice = Concept([charParam], "isInPIOffice")
isDead = Concept([charParam], "isDead")
isArrested = Concept([charParam], "isArrested")
isArmed = Concept([charParam], "isArmed")

kickedOutClient = Concept([], "kickedOutClient")
piGotRobbed = Concept([], "piGotRobbed")
burglarsHungOutAtBar = Concept([], "burglarsHungOutAtSeedyBar")

fatherHungOutAtBar = Concept([], "fatherHungOutAtSeedyBar")
atSeedyBar = Concept([], "atSeedyBar")
talkingToMysteriousWoman = Concept([], "talkingToMysteriousWoman")

isObsessive = Concept([charParam], "isObessive")

wifeDiedRandomly = Concept([charParam], "wifeDiedRandomly")
regainFaith = Concept([charParam], "regainFaith")

politicalScandal = Concept([], "politicalScandal")
foundMotive = Concept([], "foundMotive")

narrative_pieces = (
    [
        MakeBeat("Introduce PI")
            .if_not(storyStart)
            .sets_up(storyStart, characterIsPI(1), isInPIOffice(1)),

        MakeBeat("PI is protagonist")
            .ok_if(storyStart, characterIsPI(1))
            .if_not(isProtag(any1))
            .sets_up(isProtag(1)),

        MakeBeat("Reads political scandal in paper")
            .ok_if(isInPIOffice(0), isProtag(0))
            .sets_up(politicalScandal),

        MakeBeat("Introduce dead brother")
            .if_not(characterHasDeadBrother(any1))
            .if_not(heros_journey.ghost)
            .ok_if(isProtag(0))
            .sets_up(characterHasDeadBrother(0), heros_journey.you, heros_journey.ghost),

        MakeBeat("Client walks in")
            .if_not(isInPIOffice(any1), isClient(any1)) # for any other char
            .if_not(characterIsPI(1))
            .if_not(hasACase(0))
            .ok_if(characterIsPI(0), isInPIOffice(0))
            .sets_up(isInPIOffice(1), isClient(1)),

        MakeBeat("PI tells client they love them. Client goes home. PI goes home")
            .ok_if(characterIsPI(0), isInPIOffice(1), isClient(1), heros_journey.ghost)
            .sets_up(isCreepy(0), isHome(0), heros_journey.need),

        MakeBeat("Yells at client to get out. Goes home.")
            .ok_if(characterIsPI(0), isInPIOffice(1), isClient(1), heros_journey.ghost)
            .sets_up(kickedOutClient, isHome(0), heros_journey.need),

        MakeBeat("Father missing case")
            .ok_if(characterIsPI(0), isInPIOffice(1), isClient(1), heros_journey.ghost)
            .if_not(hasACase(0))
            .sets_up(hasACase(0), caseOfMissingFather(0), heros_journey.need),

        MakeBeat("Takes gun out of desk")
            .ok_if(isInPIOffice(0), isProtag(0))
            .sets_up(isArmed(0)),

        MakeBeat("Someone robs PI")
            .if_not(hasACase(0))
            .ok_if(characterIsPI(0), isHome(0))
            .sets_up(piGotRobbed, hasACase(0)),

        MakeBeat("Finds matchbox from burglars")
            .ok_if(piGotRobbed)
            .sets_up(burglarsHungOutAtBar, heros_journey.go),

        MakeBeat("Has big conspiracy board with yarn and stuff")
            .if_not(hasGuidance(0, any1))
            .ok_if(isInPIOffice(0), isProtag(0), hasACase(0), heros_journey.need)
            .sets_up(isObsessive(0)),

        MakeBeat("Asks old boss for help")
            .ok_if(hasACase(1), heros_journey.need)
            .if_not(isObsessive(1)) # because leads to contradictory endoings
            .if_not(isProtag(2))
            .if_not(isClient(2))
            .if_not(hasGuidance(1,any1))
            .sets_up(hasGuidance(1, 2)),

        MakeBeat("Breaks into father's appartment.")
            .ok_if(isObsessive(1), caseOfMissingFather(1))
            .ok_if(hasGuidance(1,2), caseOfMissingFather(1))
            .sets_up(inFathersAppartment(1)),

        MakeBeat("Finds father dead.")
            .ok_if(inFathersAppartment(1))
            .sets_up(foundDeadFather(1), heros_journey.go),

        MakeBeat("Finds matchbox on father's body.")
            .ok_if(foundDeadFather(1), heros_journey.go)
            .sets_up(fatherHungOutAtBar),

        MakeBeat("Goes to seedy bar.")
            .ok_if(fatherHungOutAtBar)
            .ok_if(burglarsHungOutAtBar)
            .sets_up(atSeedyBar),

        MakeBeat("Listens to nightclub singer. Realizes it's a coded message")
            .ok_if(atSeedyBar)
            .sets_up(secretMessageSinger),

        MakeBeat("Talks to mysterious woman.")
            .ok_if(atSeedyBar)
            .sets_up(talkingToMysteriousWoman),

        # sets up for character change at the end, this is needed to accept
        # that the mentor was a bad guy
        MakeBeat("Mystery woman says dead father betrayed his own brother and "
            + "you have to accept loss.")
            .ok_if(characterHasDeadBrother(1), talkingToMysteriousWoman)
            .sets_up(heros_journey.find),

        # sets up for character change at the end
        MakeBeat("Mystery woman says dead father had no faith but you have to have faith.")
            .ok_if(wifeDiedRandomly(1), talkingToMysteriousWoman, caseOfMissingFather(1))
            .sets_up(heros_journey.find),

        # TODO: follow up with watching them perform a ritual that fails.
        # TODO: if supernatural established then maybe could be real
        MakeBeat("Finds out that dead father was in satanic cult.")
            .ok_if(heros_journey.find, caseOfMissingFather(1))
            .sets_up(foundMotive, satanicCult),

        MakeBeat("Overhears that dead father was involved in scandal.")
            .ok_if(heros_journey.find, politicalScandal, caseOfMissingFather(1))
            .sets_up(foundMotive),

        MakeBeat("Finds evidence criminal mastermind did it.")
            .ok_if(foundMotive, isObsessive(1))
            .sets_up(foundEvidenceOfPerp(1,2), isPerp(2), heros_journey.take),

        # TODO: need to expand on this
        MakeBeat("Finds evidence his old boss did it.")
            .ok_if(foundMotive, hasGuidance(1,2))
            .sets_up(foundEvidenceOfPerp(1,2), isPerp(2), heros_journey.take),

        MakeBeat("Goes to perps place.")
            .ok_if(foundEvidenceOfPerp(1,2), heros_journey.take)
            .sets_up(isAtHouse(1,2)),

        MakeBeat("Perp sees PI and bolts.")
            .ok_if(isAtHouse(0,1), isPerp(1))
            .sets_up(runsAway(1)),

        MakeBeat("PI chases perp.")
            .ok_if(runsAway(1), isAtHouse(2,1))
            .sets_up(chasing(1, 2)),

        MakeBeat("PI is shot in shoulder by perp while running")
            .ok_if(chasing(1, 2), isArmed(2), isProtag(2))
            .sets_up(protagGotShot, heros_journey.theReturn),

        MakeBeat("Frog 1 is here and I'm going to get him..")
            .ok_if(chasing(1, 2), isObsessive(2))
            .sets_up(story_end),

        MakeBeat("Perp gets cornered down an alley.")
            .if_not(isObsessive(2))
            .ok_if(chasing(1,2))
            .sets_up(cornered(1,2)),

        MakeBeat("Perp pulls a gun. Fires on our hero and misses. PI kills perp.")
            .ok_if(cornered(1, 2), isArmed(2))
            .sets_up(isDead(1)),

        MakeBeat("Protag throws gun away")
            .ok_if(protagGotShot, isArmed(1), isProtag(1))
            .sets_up(heros_journey.change),

        MakeBeat("Client learns who kidnapped/killed father and thanks PI for closure")
            .ok_if(isPerp(1), isArrested(1), heros_journey.change)
            .ok_if(isPerp(1), isDead(1), heros_journey.change)
            .sets_up(story_end),

        MakeBeat("Wife died suddenly. Her last words didn't mean anything.")
            .if_not(wifeDiedRandomly(any1))
            .if_not(heros_journey.ghost)
            .sets_up(wifeDiedRandomly(1), heros_journey.ghost),

        MakeBeat("Wife last words become meaningful.")
            .ok_if(wifeDiedRandomly(1), heros_journey.theReturn)
            .sets_up(regainFaith(1), heros_journey.change),
    ]
)

#TODO: concept, children's story logic.

#TODO: if farther from home -> sparser homes. Pavement is cracked up

discreteToContinuous = Concept([], "discrete")
knowPerpIsInChinatown = Concept([], "knowIsInChinatown")

to_add_later = (
    [
        MakeBeat("You should first describe my life by how I overcame a youthful obsession " +
            "with discrete mathematics and found love with continuous values. Real beauty exists " +
            "again within itself and does not stop at some arbitrary depth.")
            .sets_up(discreteToContinuous),
        MakeBeat("Forget it Jake, it's Chinatown.")
            .ok_if(knowPerpIsInChinatown)
            .sets_up(story_end),
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
