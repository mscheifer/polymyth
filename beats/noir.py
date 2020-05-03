from story import (
    any1,
    Concept,
    NarrativePiece,
    MakeBeat,
    story_end
)
from beats.character_arcs import ProtagonistDefinition, HerosJourney

import expression.actions as actions
import expression.descriptions as descriptions
import expression.modifiers as modifiers
import expression.nouns as nouns
import prose

# Parm types
charParam = 'char_param_type'
locationParam = "location_param_type"

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

isPI = Concept([charParam], "isPI")
isRamenShopOwner = Concept([charParam], "isRamenShopOwner")
isFormerCop = Concept([charParam], "isFormerCop")
isFormerOpiumAdict = Concept([charParam], "isFormerOpiumAdict")
isAwkward = Concept([charParam], "isAwkward")
isCocky = Concept([charParam], "isCocky")
hasDeadBrother = Concept([charParam], "deadBro")
hasACase = Concept([charParam], "hasACase")
isProtag = Concept([charParam], "isProtag")
isCreepy = Concept([charParam], "isCreepy")
isPerp = Concept([charParam], "isPerp")
isClient = Concept([charParam], "isClient")
isObsessive = Concept([charParam], "isObessive")
isParanoid = Concept([charParam], "isParanoid")
isInsecure = Concept([charParam], "isInsecure")

#TODO: these should be stateful
isChainedUp = Concept([charParam], "isChainedUp")
isFree = Concept([charParam], "isFree")

died = Concept([charParam], "died")
gotArrested = Concept([charParam], "gotArrested")
gotAGun = Concept([charParam], "gotAGun")
protagGotShot = Concept([], "protagGotShot")

kickedOutClient = Concept([charParam, charParam], "kickedOutClient")
protagGotRobbed = Concept([], "piGotRobbed")

burglarsHungOutAtBar = Concept([locationParam], "burglarsHungOutAtBar")
fatherHungOutAtBar = Concept([locationParam], "fatherHungOutAtBar")
talkedToMysteriousWoman = Concept([], "talkedToMysteriousWoman")

wifeDiedRandomly = Concept([charParam], "wifeDiedRandomly")
regainFaith = Concept([charParam], "regainFaith")

politicalScandal = Concept([], "politicalScandal")
satanicCult = Concept([], "satanicCult")
secretMessageSinger = Concept([], "secretMessageSinger")
foundMotive = Concept([], "foundMotive")
heardCodedWords = Concept([], "heardCodedWords")
dogCanFindKeys = Concept([], "dogCanFindKeys")
knowPerpIsInChinatown = Concept([], "knowIsInChinatown")

needsToHelpMom = Concept([charParam], "needsToHelpMom")
wasRejectedForDate = Concept([charParam], "wasRejectedForDate")
askOutAfterManyDates = Concept([charParam], "askOutAfterManyDates")
wantsToFightWaiter = Concept([charParam], "wantsToFightWaiter")

tripping = Concept([charParam], "tripping")
tripyExistentialCrisis = Concept([charParam], "tripyExistentialCrisis")

# Locations
isUnknownLoc = Concept([locationParam], "unknown loc")
isPIOffice = Concept([locationParam], "PI office")
isRamenShop = Concept([locationParam], "Ramen shop")
isProtagHome = Concept([locationParam], "PI home")
isBar = Concept([locationParam], "bar")
isStreets = Concept([locationParam], "streets")

# TODO: make stateful
isOnPhone = Concept([charParam], "isOnPhone")

nowAtLocation = Concept(
    [charParam], "nowAtLocation", value_parameter_types=[locationParam]
)
def nowAt(character, location):
    return nowAtLocation.current([character], [location])

#TODO:
# if early scene mentioned stamp collecting offhandedly
# then search for missing money turns out it was turned into rare stamps and
# hidden in plain sight

narrative_pieces = ([
    MakeBeat("Introduce PI")
        # Need to establish protagonist before this phase is done
        .if_not(HerosJourney.you)
        .if_not(isProtag(any1))
        .express(actions.lean_back_in_chair)
        .sets_up(isProtag(1), isPI(1), nowAt(1, 2), isPIOffice(2)),

    MakeBeat("Introduce PI on phone")
        .ok_if(isPI(1), nowAt(1, 2), isPIOffice(2))
        .express(actions.twirl_phone_cord)
        .sets_up(isOnPhone(1)),

    MakeBeat("PI is awkward, we learn from asking out on phone call")
        .ok_if(isPI(1), isOnPhone(1))
        .if_not(isCocky(1), wifeDiedRandomly(1))
        .express(actions.ask_what_are_you_up_to_this_weekend, 1)
        .express(actions.say_oh_not_much, 2)
        .express(
            actions.ask_if_want,
            nouns.on_a_date,
            modifiers.again,
            modifiers.specific_time,
            1,
            2
        )
        .sets_up(isAwkward(1), needsToHelpMom(1)),

    MakeBeat("PI rejected")
        .ok_if(isAwkward(1))
        .express(actions.get_rejected, 1)
        .sets_up(wasRejectedForDate(1)),

    MakeBeat("PI wants to fight waiter")
        .ok_if(isPI(1), isOnPhone(1))
        .if_not(isAwkward(1))
        .express(actions.talk_about_fight_waiter, 1, 2)
        .sets_up(askOutAfterManyDates(1)),

    MakeBeat("PI is cocky")
        .ok_if(isPI(1), isOnPhone(1), wantsToFightWaiter(1))
        .express(actions.be_cocky_on_phone)
        .sets_up(isCocky(1)),

    MakeBeat("Introduce Ramen shop owner")
        .express(descriptions.opened_shop_late_at_night)
        .express(descriptions.served_late_night_customers)
        # Need to establish protagonist before this phase is done
        .if_not(HerosJourney.you)
        .if_not(isProtag(any1))
        .sets_up(isProtag(1), isRamenShopOwner(1), nowAt(1, 2), isRamenShop(2)),

    #TODO: resolution to this arc is coming to terms with himself "I am as much
    # as I am"
    MakeBeat("Former cop. Kicked off force due to alcoholism. Hates self for"
        + " it.")
        .if_not(ProtagonistDefinition.ghost)
        .sets_up(isFormerCop(1), ProtagonistDefinition.ghost),

    MakeBeat("Reads political scandal in paper")
        .express(actions.open_paper)
        .express(actions.read_political_scandal_in_paper, 0)
        .ok_if(nowAt(0, 1), isPIOffice(1), isProtag(0))
        .sets_up(politicalScandal),

    MakeBeat("Introduce dead brother")
        .if_not(hasDeadBrother(any1))
        .if_not(ProtagonistDefinition.ghost)
        .ok_if(isProtag(0))
        .sets_up(
            hasDeadBrother(0), HerosJourney.you, ProtagonistDefinition.ghost
        ),

    # TODO: similar scene but regular customer of ramen shop comes in with
    # problem
    MakeBeat("Client walks in")
        .express(actions.see_client_walk_in)
        .if_not(nowAt(any1, 2), isClient(any1)) # for any other char
        .if_not(hasACase(0))
        .if_not(isPI(1))
        .ok_if(isPI(0), nowAt(0, 2), isPIOffice(2))
        .sets_up(nowAt(1, 2), isClient(1)),

    MakeBeat("PI tells client they love them. Client goes home. PI leaves")
        .ok_if(isPI(0), isClient(1), nowAt(0, 2), nowAt(1, 2), isPIOffice(2), ProtagonistDefinition.ghost)
        .if_not(isPIOffice(3))
        .sets_up(isCreepy(0), nowAt(0, 3), isUnknownLoc(3), HerosJourney.need),

    MakeBeat("Yells at client to get out. Leaves.")
        .ok_if(isPI(0), isClient(1), nowAt(0, 2), nowAt(1, 2), isPIOffice(2), ProtagonistDefinition.ghost)
        .if_not(isPIOffice(3))
        .sets_up(kickedOutClient(0,1), nowAt(0, 3), isUnknownLoc(3), HerosJourney.need),

    MakeBeat("Don't care what you think, eye roll.")
        .express(actions.say_i_stopped_caring_what_people_think, 0)
        .express(actions.roll_eyes, 1)
        .express(actions.look_hurt, 0)
        .ok_if(isCocky(0))
        .sets_up(isInsecure(0)),

    #TODO: somehow have leaving the office possibly lead to walking home or cut
    # straight to being home

    MakeBeat("#0 Walks home in the rain. Sees shadows of people following them.")
        .express(actions.walk_to, 0, nouns.home, modifiers.in_rain)
        .express(actions.see_shadows_of_people_following, 0)
        .ok_if(isProtag(0), nowAt(0, 1), isUnknownLoc(1))
        .sets_up(isParanoid(0), nowAt(0, 2), isStreets(2)),

    MakeBeat("Goes home.")
        .ok_if(isProtag(0), nowAt(0, 1), isStreets(1))
        .sets_up(nowAt(0, 2), isProtagHome(2)),

    MakeBeat("Watches talk show. Guest jokes about ghosting.")
        .ok_if(isProtag(0), nowAt(0, 1), isProtagHome(1))
        .express(actions.turn_on, 0, nouns.television)
        .express(actions.watch_talk_show_about_ghosting)
        .sets_up(),

    MakeBeat("Father missing case")
        .ok_if(isPI(0), nowAt(0, 2), isPIOffice(2), isClient(1), nowAt(1, 2), ProtagonistDefinition.ghost)
        .if_not(hasACase(0))
        .express(actions.hear_client_father_is_missing)
        .sets_up(hasACase(0), caseOfMissingFather(0), HerosJourney.need),

    # TODO: next beat here would be to be fake guest at party and try to
    # eavesdrop on father talking to shady people
    MakeBeat("Father being shady case")
        .ok_if(
            isPI(0),
            nowAt(0, 2),
            isPIOffice(2),
            isClient(1),
            nowAt(1, 2),
            ProtagonistDefinition.ghost
        )
        .if_not(hasACase(0))
        .sets_up(hasACase(0), HerosJourney.need),

    MakeBeat("Takes gun out of desk")
        .express(actions.take_gun_out_of_desk, 0)
        .ok_if(nowAt(0, 1), isPIOffice(1), isProtag(0))
        .sets_up(gotAGun(0)),

    #TODO: character arc for awkward version is that he has to make a difficult
    # decision at climax and be confident
    #TODO: Character arc for cocky version is?

    MakeBeat("Wakes up disheveled. Asks dog to find keys while getting dressed.")
        .ok_if(nowAt(0, 1), isProtagHome(1))
        .sets_up(dogCanFindKeys),

    MakeBeat("Someone robs Protag")
        .if_not(hasACase(0))
        .ok_if(isProtag(0), nowAt(0, 1), isProtagHome(1))
        .sets_up(protagGotRobbed, hasACase(0)),

    MakeBeat("PI slept and dreamed of heroin.")
        .if_not(ProtagonistDefinition.ghost)
        .ok_if(isPI(0), nowAt(0, 1), isProtagHome(1))
        .sets_up(isFormerOpiumAdict(0), ProtagonistDefinition.ghost),

    MakeBeat("Finds matchbox from burglars")
        .ok_if(protagGotRobbed)
        .if_not(isPIOffice(1))
        .if_not(isProtagHome(1))
        .sets_up(burglarsHungOutAtBar(1), isBar(1), HerosJourney.go),

    MakeBeat("Has big conspiracy board with yarn and stuff")
        .if_not(hasGuidance(0, any1))
        .ok_if(nowAt(0, 1), isPIOffice(1), isProtag(0), hasACase(0), HerosJourney.need)
        .sets_up(isObsessive(0)),

    MakeBeat("Asks old boss for help")
        .ok_if(hasACase(1), HerosJourney.need)
        .if_not(isObsessive(1)) # because leads to contradictory endings
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
        .sets_up(foundDeadFather(1), HerosJourney.go),

    MakeBeat("Finds matchbox on father's body.")
        .ok_if(foundDeadFather(0), HerosJourney.go)
        .if_not(isPIOffice(1))
        .if_not(isProtagHome(1))
        .sets_up(fatherHungOutAtBar(1), isBar(1)),

    MakeBeat("Finds paper with non-sensical phrases.")
        .ok_if(foundDeadFather(0), HerosJourney.go)
        .sets_up(heardCodedWords),

    MakeBeat("Goes to seedy bar.")
        .ok_if(fatherHungOutAtBar(1), isPI(0))
        .ok_if(burglarsHungOutAtBar(1), isPI(0))
        .if_not(nowAt(0, any1), isBar(any1))
        .sets_up(nowAt(0, 1)),

    #TODO: if isAwkward(1) scene where someone is talking about a standoff with
    # police because a guy was accused of selling weapons out of shop, and 1
    # asks if that was true. There's an awkward silence and someone jokingly
    # asks if he's a cop and pats him on the head

    #TODO: PI is tailing someone. Follows them into a movie theater.
    # Movie that is playing is thematic
    # Thinks he sees the person sit down next to someone else. They look like
    # they're exchanging something, but it's hard to see.
    # Later in the story it turns out something else was happening.

    MakeBeat("Listens to nightclub singer. Realizes it's a coded message")
        .ok_if(nowAt(0, 1), isBar(1), heardCodedWords)
        .sets_up(secretMessageSinger),

    MakeBeat("Mom calls and talks for a long time while he just gives meeker"
        + " and shorter answers")
        .ok_if(isAwkward(1))
        .sets_up(),

    # TODO: this could also be a fortune teller, so not at the bar
    MakeBeat("Talks to mysterious woman.")
        .ok_if(nowAt(0, 1), isBar(1))
        .sets_up(talkedToMysteriousWoman),

    # sets up for character change at the end, this is needed to accept
    # that the mentor was a bad guy
    MakeBeat("Mystery woman says dead father betrayed his own brother and "
        + "you have to accept loss.")
        .ok_if(hasDeadBrother(1), talkedToMysteriousWoman)
        .sets_up(HerosJourney.find),

    # sets up for character change at the end
    MakeBeat("Mystery woman says dead father had no faith but you have to have faith.")
        .ok_if(wifeDiedRandomly(1), talkedToMysteriousWoman, caseOfMissingFather(1))
        .sets_up(HerosJourney.find),

    # TODO: follow up with watching them perform a ritual that fails.
    # TODO: if supernatural established then maybe could be real
    MakeBeat("Finds out that dead father was in satanic cult.")
        # Require PI is obsessive for thematic reasons
        .ok_if(HerosJourney.find, isObsessive(1), caseOfMissingFather(1))
        .sets_up(foundMotive, satanicCult),

    MakeBeat("Overhears that dead father was involved in scandal.")
        .ok_if(HerosJourney.find, politicalScandal, caseOfMissingFather(1))
        .sets_up(foundMotive),

    MakeBeat("Finds evidence criminal mastermind did it.")
        .ok_if(foundMotive, isObsessive(1))
        .sets_up(foundEvidenceOfPerp(1,2), isPerp(2), HerosJourney.take),

    MakeBeat("Dog finds keys to free PI.")
        .ok_if(isChainedUp(0), isPI(0), dogCanFindKeys)
        .sets_up(isFree(0)),

    # TODO: need to expand on this
    MakeBeat("Finds evidence his old boss did it.")
        .ok_if(foundMotive, hasGuidance(1,2))
        .sets_up(foundEvidenceOfPerp(1,2), isPerp(2), HerosJourney.take),

    # TODO: if PI's ghost is a fear of placeA, final showdown should be at
    # placeA

    # TODO: if antagonist has pretended to be someone else, final showdown in
    # house of mirrors

    MakeBeat("Goes to perps place.")
        .ok_if(foundEvidenceOfPerp(1,2), HerosJourney.take)
        .sets_up(isAtHouse(1,2)),

    MakeBeat("Perp sees PI and bolts.")
        .ok_if(isAtHouse(0,1), isPerp(1))
        .sets_up(runsAway(1)),

    MakeBeat("PI chases perp.")
        .ok_if(runsAway(1), isAtHouse(2,1))
        .sets_up(chasing(1, 2)),

    MakeBeat("PI is shot in shoulder by perp while running")
        .ok_if(chasing(1, 2), gotAGun(2), isProtag(2))
        .sets_up(protagGotShot, HerosJourney.theReturn),

    MakeBeat("Frog 1 is here and I'm going to get him..")
        .ok_if(chasing(1, 2), isObsessive(2))
        .sets_up(story_end),

    MakeBeat("Perp gets cornered down an alley.")
        .if_not(isObsessive(2))
        .ok_if(chasing(1,2))
        .sets_up(cornered(1,2)),

    MakeBeat("Perp pulls a gun. Fires on our hero and misses. PI kills perp.")
        .ok_if(cornered(1, 2), gotAGun(2))
        .sets_up(died(1)),

    MakeBeat("Protag throws gun away")
        .ok_if(protagGotShot, gotAGun(1), isProtag(1))
        .sets_up(HerosJourney.change),

    MakeBeat("Client learns who kidnapped/killed father and thanks PI for closure")
        .ok_if(isPerp(1), gotArrested(1), HerosJourney.change)
        .ok_if(isPerp(1), died(1), HerosJourney.change)
        .sets_up(story_end),

    MakeBeat("Wife died suddenly. Her last words didn't mean anything.")
        .if_not(wifeDiedRandomly(any1))
        .if_not(ProtagonistDefinition.ghost)
        .if_not(isAwkward(1))
        .sets_up(wifeDiedRandomly(1), ProtagonistDefinition.ghost),

    MakeBeat("Wife last words become meaningful.")
        .ok_if(wifeDiedRandomly(1), HerosJourney.theReturn)
        .sets_up(regainFaith(1), HerosJourney.change),

    MakeBeat("Forget it Jake, it's Chinatown.")
        .ok_if(knowPerpIsInChinatown)
        .sets_up(story_end),

    #TODO: character change: learns that desires to kiss girlfriend on beach
    # aren't about any real person, just ideas from movies

    MakeBeat("Client's father was a member of a secret society. Society was "
        + "bringing in shipments of drug (not illegal, just unknown). PI "
        + "accidentally takes some. Runs off in delerium, seeing things.")
        .ok_if(HerosJourney.search, isProtag(0), isPI(0))
        .sets_up(tripping(0)),

    MakeBeat("PI wakes up, his office is missing and nobody remembers him. He "
        + "takes the drug again and it all comes back")
        .ok_if(isPI(0), tripping(0))
        .sets_up(tripyExistentialCrisis(0)),

    MakeBeat("It was real. The PI learns that he is a small thing in a big "
        + "indifferent world he will never understand. He find's clients father"
        + "who says 'go home, little man'.")
        .ok_if(tripyExistentialCrisis(0))
        .sets_up(story_end),
])

#TODO: making choices for the PI to be violent -> endping where the PI turns out
# to be the murderer

free_characters = frozenset([
    prose.Character("He", "him", "his", "Alan"),
    prose.Character("She", "her", "her", "Sarah"),
    prose.Character("He", "him", "his", "David"),
    prose.Character("She", "her", "her", "Julie"),
])
free_locations = frozenset(["locA", "locB", "locC", "locD", "locE"])

free_arguments = {charParam:free_characters, locationParam:free_locations}

#TODO: generally -> character may do thing in scene because of trait -> characters doing actions can
# create a theme. Setting for action can be caused by another theme.
# farther from starting point (theme) -> road is broken up and overgrown (description).
# rocky road, character has no brains (both description) -> character falls into pot hole (action)
# character fallen down (description) -> dorthy helps them up (action)
# dorthy helps people (deescription) -> thematic conclusion where she is rewarded (theme)
