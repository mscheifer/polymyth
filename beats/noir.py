from story import (
    Concept,
    ContentPack,
    MakeBeat,
    NarrativePiece,
    Object,
    any1,
    story_end
)
from beats.character_arcs import ProtagonistDefinition, HerosJourney
from beats.core import is_character, is_location, now_at

import expression.actions as actions
import expression.descriptions as descriptions
import expression.humans as humans
import expression.modifiers as modifiers
import expression.nouns as nouns
import prose

silly_tone = Concept(0, "sillyTone")
serious_tone = Concept(0, "seriousTone")

asked_how_was_your_father = Concept(0)
asked_if_father_left_town = Concept(0)
caseOfMissingFather = Concept(1, "missingFather")

# 1st parameter is the detective, 2nd is mentor
# The params are exclusive because you can't get advice from yourself.
hasGuidance = Concept(2, "hasGuidance", is_exclusive=True)
doesnt_take_client_seriously = Concept(0)

# 1st parameter is the detective
inFathersAppartment = Concept(1, "inFathersAppartment")
# 1st parameter is the detective
foundDeadFather = Concept(1, "foundDeadFather")
# 1st parameter is the detective, 2nd param is the perp
foundEvidenceOfPerp = Concept(2, "foundEvidenceOfPerp", is_exclusive=True)
# 1st parameter is the detective, 2nd param is the perp
isAtHouse = Concept(2, "isAtHouse")
# 1st parameter is the perp
runsAway = Concept(1, "runsAway")
# 1st parameter is the perp, 2nd param is the detective
chasing = Concept(2, "chasing")
# 1st parameter is the perp, 2nd param is the detective
cornered = Concept(2, "cornered")
# 1st parameter is the detective
selfDefenseKillPerp = Concept(1, "selfDefenseKillPerp")
# 1st parameter is the detective
closure = Concept(1, "closure")

is_regular = Concept(1, "isRegular")
isPI = Concept(1, "isPI")
isRamenShopOwner = Concept(1, "isRamenShopOwner")
isFormerCop = Concept(1, "isFormerCop")
isFormerOpiumAdict = Concept(1, "isFormerOpiumAdict")
isAwkward = Concept(1, "isAwkward")
isCocky = Concept(1, "isCocky")
hasDeadBrother = Concept(1, "deadBro")
hasACase = Concept(1, "hasACase")
isProtag = Concept(1, "isProtag")
isCreepy = Concept(1, "isCreepy")
isPerp = Concept(1, "isPerp")
isClient = Concept(1, "isClient")
isObsessive = Concept(1, "isObessive")
isParanoid = Concept(1, "isParanoid")
isInsecure = Concept(1, "isInsecure")

#TODO: these should be stateful
isChainedUp = Concept(1, "isChainedUp")
isFree = Concept(1, "isFree")

died = Concept(1, "died")
gotArrested = Concept(1, "gotArrested")
gotAGun = Concept(1, "gotAGun")
protagGotShot = Concept(0, "protagGotShot")

kickedOutClient = Concept(2, "kickedOutClient")
protagGotRobbed = Concept(0, "piGotRobbed")

burglarsHungOutAtBar = Concept(0, "burglarsHungOutAtBar")
fatherHungOutAtBar = Concept(0, "fatherHungOutAtBar")
talkedToMysteriousWoman = Concept(0, "talkedToMysteriousWoman")

wifeDiedRandomly = Concept(1, "wifeDiedRandomly")
regainFaith = Concept(1, "regainFaith")

politicalScandal = Concept(0, "politicalScandal")
satanicCult = Concept(0, "satanicCult")
secretMessageSinger = Concept(0, "secretMessageSinger")
foundMotive = Concept(0, "foundMotive")
heardCodedWords = Concept(0, "heardCodedWords")
asked_dog_to_find_keys = Concept(0, "askedDogToFindKeys")
dogCanFindKeys = Concept(0, "dogCanFindKeys")
knowPerpIsInChinatown = Concept(0, "knowIsInChinatown")

needsToHelpMom = Concept(1, "needsToHelpMom")
wasRejectedForDate = Concept(1, "wasRejectedForDate")
askOutAfterManyDates = Concept(1, "askOutAfterManyDates")
wantsToFightWaiter = Concept(1, "wantsToFightWaiter")

tripping = Concept(1, "tripping")
tripyExistentialCrisis = Concept(1, "tripyExistentialCrisis")

told_to_focus_on_where_people_are = Concept(0, "toldToFocusOnWherePeopleAre")
saw_missing_father_head_to_bar = Concept(0, "sawMissingFatherHeadToBar")

alan =  Object("alan")
david = Object("david")
julie = Object("julie")
sarah = Object("sarah")

bar = Object("bar")
on_a_date = Object("bar")
pi_home = Object("pi_home")
pi_office = Object("pi_office")
ramen_shop = Object("ramen_shop")
the_streets = Object("the_streets")
unknown_location = Object("unknown_location")

objects = [
    alan,
    david,
    julie,
    sarah,

    bar,
    on_a_date,
    pi_home,
    pi_office,
    ramen_shop,
    the_streets,
    unknown_location,
]

#TODO:
# if early scene mentioned stamp collecting offhandedly
# then search for missing money turns out it was turned into rare stamps and
# hidden in plain sight

pre_established_concepts = [
    is_character(alan),
    is_character(david),
    is_character(julie),
    is_character(sarah),
    is_location(bar),
    is_location(pi_home),
    is_location(pi_office),
    is_location(ramen_shop),
    is_location(the_streets),
    is_location(unknown_location),
]

object_expressions = {
    alan: humans.man("Alan"),
    david: humans.man("David"),
    julie: humans.woman("Julie"),
    sarah: humans.woman("Sarah"),
    bar: nouns.bar,
    on_a_date: nouns.on_a_date,
    pi_home: nouns.home,
    pi_office: nouns.office,
    ramen_shop: nouns.ramen_shop,
    the_streets: nouns.the_streets,
    unknown_location: nouns.unknown_location,
}

nobody = Object("nobody")

talking_on_phone_concept = Concept(
    1, "talkingOnPhone", num_value_parameters=1
)
def talking_on_phone(character1, character2):
    return talking_on_phone_concept.current([character1], [character2])

narrative_pieces = ([
    MakeBeat("Introduce PI")
        # Need to establish protagonist before this phase is done
        .if_not(HerosJourney.you)
        .if_not(isProtag(any1))
        .ok_if(is_character(1))
        .express(actions.lean_back_in_chair, {"person": 1})
        .sets_up(isProtag(1), isPI(1), now_at(1, pi_office)),

    MakeBeat("Introduce PI on phone")
        .ok_if(isPI(1), now_at(1, pi_office), is_character(2))
        .if_not(now_at(any1, pi_office), isClient(any1))
        .express(actions.twirl_phone_cord, {"person": 1})
        .sets_up(talking_on_phone(1,2)),

    MakeBeat("PI is awkward, we learn from asking out on phone call")
        .ok_if(isPI(1), talking_on_phone(1,2))
        .if_not(isCocky(1), wifeDiedRandomly(1))
        .express(actions.ask_what_are_you_up_to_this_weekend, {"person": 1})
        .express(actions.say_oh_not_much, {"person": 2})
        .express(
            actions.ask_if_want,
            {"asker": 1, "askee": 2, "thing": on_a_date},
            modifiers.again,
            modifiers.specific_time
        )
        .sets_up(isAwkward(1), needsToHelpMom(1)),

    MakeBeat("PI rejected")
        .ok_if(isAwkward(1), talking_on_phone(1,2))
        .express(actions.get_rejected, {"pi": 1, "date": 2})
        .sets_up(wasRejectedForDate(1)),

    MakeBeat("PI wants to fight waiter")
        .ok_if(isPI(1), talking_on_phone(1,2))
        .if_not(isAwkward(1))
        .express(actions.talk_about_fight_waiter, {"pi": 1, "date": 2})
        .sets_up(askOutAfterManyDates(1)),

    MakeBeat("PI is cocky")
        .ok_if(isPI(1), talking_on_phone(1,2), wantsToFightWaiter(1))
        .express(actions.be_cocky_on_phone, {"pi": 1, "date": 2})
        .sets_up(isCocky(1)),

    MakeBeat("Introduce Ramen shop owner")
        .express(descriptions.opened_shop_late_at_night, {"person": 1})
        .express(descriptions.served_late_night_customers, {"person": 1})
        # Need to establish protagonist before this phase is done
        .if_not(HerosJourney.you)
        .if_not(isProtag(any1))
        .sets_up(isProtag(1), isRamenShopOwner(1), now_at(1, ramen_shop)),

    #TODO: resolution to this arc is coming to terms with himself "I am as much
    # as I am", he does this by taking the action of going to see his mother and
    # acknowledging he is what he is. He has to acknowledge that there's some
    # good / worth in him even though he's below society's accepted level of
    # normalcy for decency and success. He hasn't seen his mother for 10 years
    # because he's afraid to tell her that he screwed up his life.
    #
    # Alternatively, if he is both he alcoholic and cocky then he should fuck up
    # the case somehow like getting the father killed at the end of the second
    # act and then in the 4th act he just admits outloud that he's a fuck up,
    # that's the growth.
    MakeBeat("Former cop. Kicked off force due to alcoholism. Hates self for"
        + " it.")
        .if_not(ProtagonistDefinition.ghost)
        .sets_up(isFormerCop(1), ProtagonistDefinition.ghost),

    MakeBeat("Reads political scandal in paper")
        .express(actions.open_paper, {"person": 0})
        .express(actions.read_political_scandal_in_paper, {"person": 0})
        .if_not(now_at(any1, pi_office), isClient(any1))
        .ok_if(now_at(0, pi_office), isProtag(0))
        .sets_up(politicalScandal),

    MakeBeat("Introduce dead brother")
        .if_not(hasDeadBrother(any1))
        .if_not(ProtagonistDefinition.ghost)
        .ok_if(isProtag(0))
        .sets_up(
            hasDeadBrother(0), HerosJourney.you, ProtagonistDefinition.ghost
        ),

    MakeBeat("Client walks in")
        .express(actions.see_client_walk_in, {"pi": 0, "client": 1})
        .if_not(now_at(any1, pi_office), isClient(any1)) # for any other char
        .if_not(hasACase(0))
        .if_not(isPI(1)) # TODO: instead speacial is_same concept
        .ok_if(isPI(0), now_at(0, pi_office))
        .sets_up(now_at(1, pi_office), isClient(1)),

    MakeBeat("Hang up because see client")
        .express(actions.hang_up, {"person": 0})
        .ok_if(now_at(1, pi_office), isClient(1), talking_on_phone(0, 1))
        .sets_up(talking_on_phone(0, nobody)),

    MakeBeat("Regular's father is missing")
        .express(actions.see_regular_walk_in, {"owner": 0, "regular": 1})
        .express(actions.hear_regular_father_is_missing, {"owner": 0, "regular": 1})
        .ok_if(isRamenShopOwner(0), now_at(0, ramen_shop), is_character(1))
        # TODO: instead of saying can't be another ramen shop owner, should have special is_same concept
        .if_not(caseOfMissingFather(0), isRamenShopOwner(1))
        .sets_up(now_at(1, ramen_shop), is_regular(1), caseOfMissingFather(0)),

    MakeBeat("Closes shop and leaves.")
        .ok_if(isRamenShopOwner(0), now_at(0, ramen_shop))
        .sets_up(now_at(0, the_streets)),

    MakeBeat("PI tells client they love them. Client goes home. PI leaves")
        .ok_if(
            isPI(0),
            isClient(1),
            now_at(0, pi_office),
            now_at(1, pi_office),
            ProtagonistDefinition.ghost
        )
        .sets_up(isCreepy(0), now_at(0, unknown_location), HerosJourney.need),

    MakeBeat("Yells at client to get out. Leaves.")
        .ok_if(
            isPI(0),
            isClient(1),
            now_at(0, pi_office),
            now_at(1, pi_office),
            ProtagonistDefinition.ghost
        )
        .sets_up(kickedOutClient(0,1), now_at(0, unknown_location), HerosJourney.need),

    MakeBeat("Don't care what you think, eye roll.")
        .express(actions.say_i_stopped_caring_what_people_think, {"person": 0})
        .express(actions.roll_eyes, {"person": 1})
        .express(actions.look_hurt, {"person": 0})
        .ok_if(isCocky(0))
        .sets_up(isInsecure(0)),

    #TODO: somehow have leaving the office possibly lead to walking home or cut
    # straight to being home

    MakeBeat("#0 Walks home in the rain. Sees shadows of people following them.")
        .express(actions.walk_to, {"person": 0, "to": pi_home}, modifiers.in_rain)
        .express(actions.see_shadows_of_people_following, {"person": 0})
        .ok_if(isProtag(0), now_at(0, unknown_location))
        .sets_up(isParanoid(0), now_at(0, the_streets)),

    MakeBeat("Goes home.")
        .ok_if(isProtag(0), now_at(0, the_streets))
        .sets_up(now_at(0, pi_home)),

    MakeBeat("Watches talk show. Guest jokes about ghosting.")
        .ok_if(isProtag(0), now_at(0, pi_home))
        .express(actions.turn_on, {"person": 0, "thing": nouns.television})
        .express(actions.watch_talk_show_about_ghosting, {"person": 0})
        .sets_up(),

    MakeBeat("Meet client have met before")
        .ok_if(
            isPI(0),
            now_at(0, pi_office),
            isClient(1),
            now_at(1, pi_office),
        )
        .express(actions.say_met_client_and_father_once_and_admire_father, {"pi": 0, "client": 1})
        .sets_up(asked_how_was_your_father),

    MakeBeat("Father missing case")
        .ok_if(
            isPI(0),
            now_at(0, pi_office),
            isClient(1),
            now_at(1, pi_office),
            ProtagonistDefinition.ghost
        )
        .if_not(hasACase(0))
        .express(actions.hear_client_father_is_missing, {"pi": 0, "client": 1})
        .sets_up(hasACase(0), caseOfMissingFather(0), HerosJourney.need),

    MakeBeat("Meet client have met before")
        .ok_if(
            isPI(0),
            now_at(0, pi_office),
            isClient(1),
            now_at(1, pi_office),
            caseOfMissingFather(0)
        )
        .express(actions.ask_if_father_left_town, {"pi": 0, "client": 1})
        .sets_up(asked_if_father_left_town, doesnt_take_client_seriously),

    # TODO: next beat here would be to be fake guest at party and try to
    # eavesdrop on father talking to shady people
    MakeBeat("Father being shady case")
        .ok_if(
            isPI(0),
            now_at(0, pi_office),
            isClient(1),
            now_at(1, pi_office),
            ProtagonistDefinition.ghost
        )
        .if_not(hasACase(0))
        .sets_up(hasACase(0), HerosJourney.need),

    MakeBeat("Takes gun out of desk")
        .express(actions.take_gun_out_of_desk, {"person": 0})
        .ok_if(now_at(0, pi_office), isProtag(0))
        #TODO: should use some special concepts to say anbody not the PI rather
        # than just checking against the client
        .if_not(now_at(any1, pi_office), isClient(any1))
        .sets_up(gotAGun(0)),

    #TODO: character arc for awkward version is that he has to make a difficult
    # decision at climax and be confident
    #TODO: Character arc for cocky version is?

    MakeBeat("Wakes up disheveled. Asks dog to find keys while getting dressed.")
        .ok_if(now_at(0, pi_home))
        .sets_up(asked_dog_to_find_keys),

    MakeBeat("Has to find keys because dog obviously can't.")
        .ok_if(asked_dog_to_find_keys)
        .sets_up(),

    MakeBeat("Dog can actually find keys.")
        .if_not(serious_tone)
        .ok_if(asked_dog_to_find_keys)
        .sets_up(dogCanFindKeys, silly_tone),

    MakeBeat("Someone robs Protag")
        .if_not(hasACase(0))
        .ok_if(isProtag(0), now_at(0, pi_home))
        .sets_up(protagGotRobbed, hasACase(0)),

    MakeBeat("PI slept and dreamed of heroin.")
        .if_not(ProtagonistDefinition.ghost)
        .ok_if(isPI(0), now_at(0, pi_home))
        .sets_up(isFormerOpiumAdict(0), ProtagonistDefinition.ghost),

    MakeBeat("Finds matchbox from burglars")
        .ok_if(protagGotRobbed)
        .sets_up(burglarsHungOutAtBar(), HerosJourney.go),

    MakeBeat("Has big conspiracy board with yarn and stuff")
        .if_not(hasGuidance(0, any1))
        .ok_if(now_at(0, pi_office), isProtag(0), hasACase(0), HerosJourney.go)
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
        .sets_up(fatherHungOutAtBar()),

    MakeBeat("Finds paper with non-sensical phrases.")
        .ok_if(foundDeadFather(0), HerosJourney.go)
        .sets_up(heardCodedWords),

    MakeBeat("Sees missing father on street and follows to seedy bar")
        .ok_if(isRamenShopOwner(0), now_at(0, the_streets))
        .if_not(saw_missing_father_head_to_bar)
        .sets_up(now_at(0, bar), saw_missing_father_head_to_bar),

    MakeBeat("Goes to seedy bar.")
        .ok_if(fatherHungOutAtBar(), isProtag(0))
        .ok_if(burglarsHungOutAtBar(), isProtag(0))
        .if_not(now_at(0, bar))
        .if_not(HerosJourney.find)
        .sets_up(now_at(0, bar)),

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
        .ok_if(now_at(0, bar), heardCodedWords)
        .sets_up(secretMessageSinger),

    MakeBeat("Mom calls and talks for a long time while he just gives meeker"
        + " and shorter answers")
        .ok_if(isAwkward(1))
        .sets_up(),

    # TODO: this could also be a fortune teller, so not at the bar
    MakeBeat("Talks to mysterious woman.")
        .ok_if(now_at(0, bar))
        .sets_up(talkedToMysteriousWoman),

    # sets up for character change at the end, this is needed to accept
    # that the mentor was a bad guy
    MakeBeat("Mystery woman says client's father betrayed his own brother and "
        + "you have to accept loss.")
        .ok_if(hasDeadBrother(1), talkedToMysteriousWoman)
        .sets_up(HerosJourney.find),

    # sets up for character change at the end
    MakeBeat("Mystery woman says dead father had no faith but you have to have faith.")
        .ok_if(wifeDiedRandomly(1), talkedToMysteriousWoman, caseOfMissingFather(1))
        .sets_up(HerosJourney.find),

    # sets up for character change at the end
    MakeBeat("Mystery woman says you are living to much in where people could" +
        " be. Focus on where they are now.")
        .ok_if(isFormerCop(1), talkedToMysteriousWoman)
        .sets_up(told_to_focus_on_where_people_are, HerosJourney.find),

    MakeBeat("Leaves seedy bar.")
        .ok_if(HerosJourney.find, now_at(0, bar))
        .sets_up(now_at(0, the_streets)),

    MakeBeat("Calls regular, says saw their father run into bar but lost him")
        .ok_if(
            now_at(0, pi_home),
            told_to_focus_on_where_people_are,
            saw_missing_father_head_to_bar
        )
        .sets_up(),

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
        .express(descriptions.picture_and_last_words, { "person": 1, "partner": 2 })
        .if_not(wifeDiedRandomly(any1))
        .if_not(ProtagonistDefinition.ghost)
        .if_not(isAwkward(1))
        .ok_if(is_character(2), now_at(1, pi_office))
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

#TODO: generally -> character may do thing in scene because of trait -> characters doing actions can
# create a theme. Setting for action can be caused by another theme.
# farther from starting point (theme) -> road is broken up and overgrown (description).
# rocky road, character has no brains (both description) -> character falls into pot hole (action)
# character fallen down (description) -> dorthy helps them up (action)
# dorthy helps people (deescription) -> thematic conclusion where she is rewarded (theme)

content_pack = ContentPack(
    objects, pre_established_concepts, narrative_pieces, object_expressions
)

# Finds wedding ring and watch on counter, assumes intended to leave family,
# actually just was about to do the dishes.
