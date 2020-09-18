# Thoughts on high level beat file structure. Would have:
# 1. Conversations
# 2. Character arcs
# 3. Mystery
# 4. noir.py - which imports and combines the others
# 5. Character traits and relationship concepts - imported by all of character
# arcs, conversations and mysteries.
#
# There would be stuff in the character arcs file that says one of these things
# needs to be established for a part of the heros journey like
# HerosJourneyArc.search . Similarly there would be rules in the mystery file
# saying certain things need to happen before HerosJourneyMystery.search and
# then in noir.py there are rules saying both are needed before the next part
# of the story can start, and then stuff in either file is gated on the plain
# HerosJourny.search .
#
# Ok. To really make this work well I need another part of the content pack
# which are like "pre-applied" rules. So for any beat that establishes some
# concepts, if we check these rules they can disallow this beat. So like
# .ok_if(x,y,z)
# .cannot_set_up(a,b,c)
# that will allow us to express things like arc pacing where we don't want to
# set up more than one wild character trait that will need an arc to resolve.
# And then separately in another file we can describe beats for how someone
# would act or speak based on character traits, without thinking about if it's
# allowed to establish new traits or not given we want a good story structure.
#
# But I'm also thinking about an alternative where we just establish all of the
# character traits in higher level beats or logic rules in the plot and arc
# files, and then the conversation / action files will only CHECK the character
# traits but never ESTABLISH them.
#
# A simpler way to do it for now would be to just have two different versions of
# each conversation beat. One if the property is established. One that checks if
# we can establish a new character trait (none has been established before) and
# then establishes it. This can be come less work than it sounds in a few ways:
# 1. We don't need to do this for all conversation beats. Only ones that could
# start a scene / conversation, or would otherwise not make sense as the very
# first clue to a trait.
# 2. We could update the MakeBeat code to allow doing .ok_if(not()) and remove
# if_not which would let us do:
# .ok_if(is_awkward(1))
# .ok_if(not(major_flaw_established(1)))
# 3. We could use some of the old looping code before doing 2 to generate two
# copies of the beat.

from story import (
    Concept,
    ContentPack,
    MakeBeat,
    MakeLogic,
    Object,
    any1,
    any2,
    are_different,
    story_end
)
from beats.character_arcs import ProtagonistDefinition, HerosJourney
from beats.core import (
    is_character, is_location, now_at, scene_can_end, scene_cannot_end
)
from beats.noir.character_arcs import *

import expression.actions as actions
import expression.descriptions as descriptions
import expression.humans as humans
import expression.modifiers as modifiers
import expression.nouns as nouns
import prose

# Mystery is just sleight of hand with descriptions. You tell the reader the
# answer but hide it in description or jokes or any writing for some other
# purpose.

silly_tone = Concept(0, "sillyTone")
serious_tone = Concept(0, "seriousTone")

# Themes
# TODO: think more about the difference between big themes where the story poses
# conflicting arguments and then implies a conclusion, vs the smaller things
# I've been calling "thematic" where the reality of the story reflect
# character's emotion or deliberately serve to reinforce their arc. Do we need
# the big themes for a successful story and is there a better name for the
# little themes?
#
# TODO: is all progress, progress? (a la jurassic park)
#
# TODO: given all the suffering in the world, is it better to either live in the
# pain, stay cooped up inside and avoid it, or just die
#
# TODO: austere world
# - nighthwaks diner
# - brutalism
# - impossible / confusing geometries
# Resolution
# - finding beauty in a mandala
# - reverence of the pristine
theme_of_money_conflict_between_siblings = Concept(0)

# Cases
caseOfMissingFather = Concept(1, "missingFather")
father_being_shady_case = Concept(0, "caseOfShadyFather")

asked_if_father_left_town = Concept(0)
are_attracted_to_each_other = Concept(2)
bar_burned_down = Concept(0)
client_is_hiding_something = Concept(0)
client_lied = Concept(0)
feels_motivated = Concept(1)
joined_mysterious_woman_at_booth = Concept(0)
has_appointment_tomorrow_morning = Concept(1)
knows_father_went_to_bar = Concept(1)
knows_is_creepy = Concept(2) # 1st knows 2nd is creepy
knows_to_check_out_docks = Concept(1)
must_call_for_alibi = Concept(2)
is_attracted_to = Concept(2) # 1st is attracted to 2nd
is_clients_father_brother = Concept(1)
is_fathers_secretary = Concept(1)
is_framed = Concept(1)
is_in_satanic_cult = Concept(1)
is_injured_in_hospital = Concept(1)
lives_with = Concept(2, "livesWith")
made_incorrect_public_accusation = Concept(1)
run_off_together = Concept(2)
stole_car = Concept(1)
suggested_father_smuggled_drugs = Concept(0)
thinks_father_wanted_to_leave_family = Concept(0)
trusts = Concept(2) # 1st trusts 2nd
wants_to_see_something_happen_tomorrow_morning = Concept(1)
was_awkward_to_fathers_secretary = Concept(0)
went_on_a_date_with = Concept(2)
wore_a_blue_rose = Concept(1)
writhed_on_the_ground = Concept(1)

doesnt_take_client_seriously = Concept(0)
# 1st parameter is the detective, 2nd is mentor
hasGuidance = Concept(2, "hasGuidance")
told_to_go_smoke_weed = Concept(0)
we_live_inside_a_dream = Concept(0)

# 1st parameter is the detective
inFathersAppartment = Concept(1, "inFathersAppartment")
# 1st parameter is the detective
foundDeadFather = Concept(1, "foundDeadFather")
# 1st parameter is the detective, 2nd param is the perp
foundEvidenceOfPerp = Concept(2, "foundEvidenceOfPerp")
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

# Generally for these concepts, they can be established by one example and then
# other beats will take them into account implying that it's an existing part of
# the character. These should be phrased as eternal traits because even as we
# change our past is still a part of us that we learn to live with. We can only
# direct our shadows to become true archetypes, we can't ignore them. For
# example: a character is still an alcoholic if they have quit drinking because
# staying sober is something they have to keep up, every day.
hasACase = Concept(1, "hasACase")
is_amnesiac = Concept(1, "isAmnesiac")
is_asshole = Concept(1, "isAsshole")
isAwkward = Concept(1, "isAwkward")
isCocky = Concept(1, "isCocky")
isCreepy = Concept(1, "isCreepy")
isClient = Concept(1, "isClient")
is_mother_of = Concept(2, "isMotherOf") # 1st is mom, 2nd is kid
is_gambler = Concept(1, "isGambler")
is_gangster = Concept(1, "isGangster")
isInsecure = Concept(1, "isInsecure")
is_inconsiderate = Concept(1, "isInconsiderate")
isObsessive = Concept(1, "isObessive")
is_old_boss = Concept(1, "isOldBoss")
isParanoid = Concept(1, "isParanoid")
isPI = Concept(1, "isPI")
isPerp = Concept(1, "isPerp")
isProtag = Concept(1, "isProtag")
is_psychopathic = Concept(1, "isPsychopathic")
isRamenShopOwner = Concept(1, "isRamenShopOwner")
is_smoker = Concept(1, "isSmoker") # This means they have a death wish
is_regular = Concept(1, "isRegular")
is_victim = Concept(1, "isVictim")
is_violent = Concept(1, "isViolent")

# These two concepts are opposites and usually only one or the other should be
# true for a character.
needs_hard_facts_to_feel_they_understand_a_situation = Concept(1)
needs_to_know_how_everyone_feels_to_feel_they_understand_a_situation = Concept(
    1
)

#TODO: these should be stateful
isChainedUp = Concept(1, "isChainedUp")
isFree = Concept(1, "isFree")

died = Concept(1, "died")
gotArrested = Concept(1, "gotArrested")
protagGotShot = Concept(0, "protagGotShot")

kickedOutClient = Concept(2, "kickedOutClient")
protagGotRobbed = Concept(0, "piGotRobbed")

burglarsHungOutAtBar = Concept(0, "burglarsHungOutAtBar")
fatherHungOutAtBar = Concept(0, "fatherHungOutAtBar")
talkedToMysteriousWoman = Concept(0, "talkedToMysteriousWoman")
fathers_secretary_left_on_vacation = Concept(0)

# Perp motives
# Love / sex
# Greed
# Revenge
# Madness
foundMotive = Concept(0, "foundMotive")

regainFaith = Concept(1, "regainFaith")

politicalScandal = Concept(0, "politicalScandal")
satanicCult = Concept(0, "satanicCult")
secretMessageSinger = Concept(0, "secretMessageSinger")
heardCodedWords = Concept(0, "heardCodedWords")
asked_dog_to_find_keys = Concept(0, "askedDogToFindKeys")
dogCanFindKeys = Concept(0, "dogCanFindKeys")
found_keys = Concept(0, "foundKeys")
knowPerpIsInChinatown = Concept(0, "knowIsInChinatown")

needsToHelpMom = Concept(1, "needsToHelpMom")
wasRejectedForDate = Concept(1, "wasRejectedForDate")
askOutAfterManyDates = Concept(1, "askOutAfterManyDates")
wantsToFightWaiter = Concept(1, "wantsToFightWaiter")

# Lowest points
# TODO: PI's junior associate is killed
# TODO: PI is framed, cops are after him
# TODO: Finds father who doesn't want to be found ("go home little man")
# TODO: Thinks it was the client who did it. Confronts her and realizes he was
# wrong
# TODO: Fire at PI office or client house destroys all evidence they have found
# so far
# TODO: They kidnap someone's child that was shown in first act

tripping = Concept(1, "tripping")
tripyExistentialCrisis = Concept(1, "tripyExistentialCrisis")

told_to_focus_on_where_people_are = Concept(0, "toldToFocusOnWherePeopleAre")
saw_missing_father_head_to_bar = Concept(0, "sawMissingFatherHeadToBar")
was_in_traumatic_awkward_situation = Concept(1, "wasInTraumaticAwkwardSituation")

alan =  Object("alan")
clementine =  Object("clementine")
david = Object("david")
julie = Object("julie")
sarah = Object("sarah")

#TODO: instead of this, add the ability to unset the concept value.
# But long term should have the engine support a time concept. What we care
# about is:
#  1. Has something ever happend (can easily put any1 in the time param) or a
#  a bound param that isn't used anywhere else.
#  2. Has something happened before something else (this needs a special
#  operator like are_different).
#  3. Did two things happen simultaneously. (This needs a special operator too)
#  (This is probably a rarer use case than the ordering one)
#  4. To facilitate this we need a special object that creates a new 'moment'
#  that is considered to be after every beat that came before. But we also want
#  to establish that something happened in the past sometimes, which means we
#  nned the ability to create a new moment but also establish that is before
#  another moment. We could do that by letting the special happens_before op be
#  used in the _sets_up part of the rule.
nobody = Object("nobody")

bar = Object("bar")
client_home = Object("client_home")
on_a_date = Object("bar")
perp_home = Object("perp_home")
pet_shop = Object("pet_shop")
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
    is_character(clementine),
    is_character(david),
    is_character(julie),
    is_character(sarah),
    is_location(bar),
    is_location(client_home),
    is_location(pi_home),
    is_location(pi_office),
    is_location(ramen_shop),
    is_location(the_streets),
    is_location(unknown_location),
]

object_expressions = {
    alan: humans.man("Alan", "Marbury"),
    clementine: humans.woman("Clementine", "DeSoto"),
    david: humans.man("David", "Polk"),
    julie: humans.woman("Julie", "Hall"),
    sarah: humans.woman("Sarah", "Wilson"),
    bar: nouns.bar,
    nobody: nouns.nobody,
    on_a_date: nouns.on_a_date,
    pi_home: nouns.home,
    pi_office: nouns.office,
    ramen_shop: nouns.ramen_shop,
    the_streets: nouns.the_streets,
    unknown_location: nouns.unknown_location,
}

talking_to_concept = Concept(
    1, "talkingTo", num_value_parameters=1
)
def talking_to(character1, character2):
    return talking_to_concept.current([character1], [character2])

talking_on_phone_concept = Concept(
    1, "talkingOnPhone", num_value_parameters=1
)
def talking_on_phone(character1, character2):
    return talking_on_phone_concept.current([character1], [character2])

has_a_gun_concept = Concept(1, "hasAGun", num_value_parameters=1)
has_a_gun_obj = Object("has_a_gun")
has_no_gun_obj = Object("has_no_gun")
def has_a_gun(character):
    return has_a_gun_concept.current([character], [has_a_gun_obj])
def has_no_gun(character):
    return has_a_gun_concept.current([character], [has_no_gun_obj])

# We don't have any refusal-of-the-call scenes because they don't work that well
# in a mystery genre. Because I already know there is a mystery that will get
# solved, I don't believe that the detective will really refuse the case as if
# so there would be no story.

high_level_beats = [
    MakeBeat("Introduce PI in office")
        .if_not(isProtag(any1))
        .ok_if(is_character(1))
        .express(actions.lean_back_in_chair, {"person": 1})
        .sets_up(isProtag(1), isPI(1), now_at(1, pi_office)),

    MakeBeat("Introduce PI at crime scene")
        .express(descriptions.pet_shop_massacre, {"pi":1})
        .express(
            actions.ask_who_could_have_killed_animals,
            {'person': 2},
            unnamed={"person": nouns.patrolman}
        )
        .if_not(isProtag(any1))
        .ok_if(is_character(1), is_character(2))
        .sets_up(isProtag(1), isPI(1), now_at(1, pet_shop)),

    MakeBeat("Finds match book at crime scene")
        .express(actions.find_matchbook_at_crime_scene, {"pi": 1})
        .ok_if(now_at(1, pet_shop))
        .sets_up(HerosJourney.you, scene_can_end),

    #TODO: I don't want the PI to come here from unknown location if they just
    # left. How can we prevent that? Tracking most recent location somehow?
    MakeBeat("PI heads to the office")
        .ok_if(isPI(1), scene_can_end)
        .sets_up(now_at(1, pi_office)),

    MakeBeat("PI is on the phone")
        .ok_if(isPI(1), now_at(1, pi_office), is_character(2))
        .if_not(now_at(any1, pi_office), isClient(any1))
        .if_not(talking_on_phone(1, any1), are_different(any1, nobody))
        .express(actions.twirl_phone_cord, {"person": 1})
        .sets_up(talking_on_phone(1, 2), talking_to(1, 2), HerosJourney.you),

    MakeBeat("PI is awkward, we learn from asking out on phone call")
        .ok_if(isPI(1), talking_on_phone(1, 2), are_different(2, nobody))
        .if_not(isCocky(1))
        # because if he was in a loving marriage once he's not that awkward
        .if_not(wifeDiedRandomly(1))
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
        .ok_if(isAwkward(1), talking_on_phone(1, 2), are_different(2, nobody))
        .express(actions.get_rejected, {"pi": 1, "date": 2})
        .sets_up(
            wasRejectedForDate(1),
            wants_to_be_in_proximity_of_someone_they_fancy(1),
            talking_on_phone(1, nobody),
            HerosJourney.need
        ),

    MakeBeat("PI wants to fight waiter")
        .ok_if(isPI(1), talking_on_phone(1,2))
        .if_not(isAwkward(1))
        .if_not(now_at(1, any1), now_at(any2, any1), isClient(any2))
        .express(actions.talk_about_fight_waiter, {"pi": 1, "date": 2})
        .sets_up(isCocky(1), askOutAfterManyDates(1)),

    MakeBeat("PI is cocky")
        .ok_if(isPI(1), talking_on_phone(1,2), wantsToFightWaiter(1))
        .express(actions.be_cocky_on_phone, {"pi": 1, "date": 2})
        .sets_up(isCocky(1), HerosJourney.need),

    MakeBeat("Introduce Ramen shop owner")
        .express(descriptions.opened_shop_late_at_night, {"person": 1})
        .express(descriptions.served_late_night_customers, {"person": 1})
        .if_not(isProtag(any1))
        .sets_up(
            isProtag(1),
            isRamenShopOwner(1),
            now_at(1, ramen_shop),
            HerosJourney.you,
            scene_cannot_end
        ),

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
        .if_not(talking_on_phone(0, any2))
        .ok_if(now_at(0, pi_office), isProtag(0))
        .sets_up(politicalScandal),

    MakeBeat("Rejects empathy attempt from coworker about dead brother")
        .express(
            actions.reject_empathy_attempt_about_brother,
            {"rejecter": 0, "empathizer": 1}
        )
        .ok_if(
            isProtag(0),
            isPI(0),
            hasDeadBrother(0),
            now_at(0, pi_office),
            is_character(1)
        )
        .ok_if(
            isProtag(0),
            isRamenShopOwner(0),
            hasDeadBrother(0),
            now_at(0, ramen_shop),
            is_character(1)
        )
        .if_not(ProtagonistDefinition.need)
        .if_not(talking_on_phone(0, any1))
        .sets_up(
            thinks_needs_to_protect_self_from_intimacy(0),
            HerosJourney.need,
            ProtagonistDefinition.need
        ),

    MakeBeat("Introduce dead brother")
        .if_not(hasDeadBrother(any1))
        .if_not(ProtagonistDefinition.ghost)
        .ok_if(isProtag(0), thinks_needs_to_protect_self_from_intimacy(0))
        .sets_up(hasDeadBrother(0), ProtagonistDefinition.ghost),

    MakeBeat("Client walks in while PI is on the phone.")
        .if_not(now_at(any1, pi_office), isClient(any1)) # for any other char
        .if_not(hasACase(0))
        .if_not(knows_is_creepy(1, 0))
        .if_not(kickedOutClient(0, 1))
        .ok_if(
            isPI(0),
            is_character(1),
            now_at(0, pi_office),
            talking_on_phone(0, 2),
            are_different(0, 1)
        )
        .sets_up(now_at(1, pi_office), isClient(1)),

    MakeBeat("Client walks in")
        .express(actions.invite_client_in, {"pi": 0})
        .if_not(now_at(any1, pi_office), isClient(any1)) # for any other char
        .if_not(hasACase(0))
        .if_not(knows_is_creepy(1, 0))
        .if_not(kickedOutClient(0, 1))
        .if_not(talking_to(0, any2))
        .ok_if(isPI(0), now_at(0, pi_office), are_different(0, 1))
        .sets_up(now_at(1, pi_office)),

    MakeBeat("Hang up because see client")
        .express(actions.hang_up, {"person": 0})
        .ok_if(
            now_at(1, pi_office),
            isClient(1),
            now_at(0, pi_office),
            isPI(0),
            talking_on_phone(0, 2)
        )
        .sets_up(talking_on_phone(0, nobody)),

    MakeBeat("Regular's father is missing")
        .express(actions.see_regular_walk_in, {"owner": 0, "regular": 1})
        .express(actions.hear_regular_father_is_missing, {"owner": 0, "regular": 1})
        .ok_if(
            isRamenShopOwner(0),
            now_at(0, ramen_shop),
            is_character(1),
            are_different(0, 1)
        )
        .if_not(caseOfMissingFather(0))
        .sets_up(
            now_at(1, ramen_shop),
            is_regular(1),
            caseOfMissingFather(0),
            scene_can_end
        ),

    MakeBeat("Notices has no wedding ring on")
        .ok_if(isAwkward(1), now_at(1, 3), now_at(2, 3), are_different(1, 2))
        .sets_up(
            saw_has_no_wedding_ring_on(1, 2),
            is_attracted_to(1, 2),
            HerosJourney.need
        ),

    MakeBeat("Closes shop and leaves.")
        .express(actions.close_ramen_shop, {"owner": 0})
        .ok_if(isRamenShopOwner(0), now_at(0, ramen_shop), scene_can_end)
        .sets_up(now_at(0, the_streets), HerosJourney.go),

    MakeBeat("PI tells client they love them. Client goes home. PI leaves")
        .ok_if(
            isPI(0),
            isClient(1),
            now_at(0, pi_office),
            now_at(1, pi_office)
        )
        .if_not(talking_on_phone(0, any1))
        .sets_up(
            isCreepy(0),
            knows_is_creepy(1, 0),
            now_at(0, unknown_location),
            now_at(1, unknown_location),
            thinks_making_others_uncomfortable_has_no_consequence(0),
            HerosJourney.need
        ),

    MakeBeat("Yells at client to get out. Leaves.")
        .ok_if(
            isPI(0),
            isClient(1),
            now_at(0, pi_office),
            now_at(1, pi_office)
        )
        .if_not(talking_on_phone(0, any1))
        .sets_up(
            kickedOutClient(0,1),
            now_at(0, unknown_location),
            now_at(1, unknown_location),
            thinks_they_need_to_lash_out_when_they_feel_uncomforable(0),
            HerosJourney.need
        ),

    MakeBeat("Don't care what you think, eye roll.")
        .express(actions.state_dont_care_what_people_think, {"person": 0})
        .express(actions.roll_eyes, {"person": 1})
        .express(actions.look_hurt, {"person": 0})
        .ok_if(isCocky(0), are_different(0, 1), talking_to(0, 1))
        .sets_up(isInsecure(0)),

    MakeBeat("Watches talk show. Guest jokes about ghosting.")
        .ok_if(isProtag(0), now_at(0, pi_home))
        .express(actions.turn_on, {"person": 0, "thing": nouns.television})
        .express(actions.watch_talk_show_about_ghosting, {"person": 0})
        .sets_up(),

    MakeBeat("Is very eager to take case")
        .ok_if(
            hasACase(0),
            now_at(0, pi_office),
            isClient(1),
            now_at(1, pi_office),
            thinks_needs_to_protect_self_from_intimacy(0)
        )
        .sets_up(
            wants_to_work_hard_to_distract_from_personal_life(0),
            HerosJourney.go
        ),

    MakeBeat("PI asks about south american maps on the wall. Client says her " +
        "father liked to sail down to South America frequently. PI suggests he"+
        " may have been drug smuggling. Client says he would never. PI asks to"+
        " check out father's boat and client says to drop it.")
        .ok_if(
            isPI(0),
            now_at(0, client_home),
            isClient(1),
            now_at(1, client_home),
            caseOfMissingFather(0)
        )
        .sets_up(suggested_father_smuggled_drugs),

    # TODO: when the PI gets information from someone, usually it's not that
    # person just voluntarily saying something useful to the case. Usually the
    # important information is some said offhandedly or the person complaining
    # ("Yeah the bar burned down. Didn't see anybody do it. Coulda been an
    # accident. Good riddence though. Now those trucks that smell like fish
    # won't be coming by at all hours"). This makes the PI realize some goods
    # from the docs were being shipped to the bar.
    #
    # Sometimes the PI can then skillfully get more information by pretending to
    # be sympathizing. "Oh yeah those TESCO trucks I hate em too. They're all
    # over town". "No these were Abraham's Fish with that big photo of a
    # fisherman. If I ever saw that guy walking down the street I'd sock him
    # without thinking twice."
    #
    # This example is in the ask_why_bar_burned_down action text.

    MakeBeat("Makes incorrect accusation unnecessarily publicly and confidently")
        .ok_if(isAwkward(0), hasACase(0), HerosJourney.search)
        .ok_if(isCocky(0), hasACase(0), HerosJourney.search)
        .if_not(talking_on_phone(0, any1))
        .sets_up(made_incorrect_public_accusation(0), HerosJourney.find),

    MakeBeat("Appologizes to client for making incorrect accusation. Offers " +
        "to resign from case. Client accepts apology and says that she found "+
        "some boxes that came in on his ship in the garage. It was odd that " +
        "they were at the house so she looked through them and found " +
        "matroishka dolls stuffed with bags of white powder. So Client keeps "+
        "PI on because he does have good instincts.")
        .ok_if(
            made_incorrect_public_accusation(0),
            suggested_father_smuggled_drugs
        )
        .sets_up(
            sincerely_applogized(0),
            learned_to_apologize_and_recover_from_mistakes(0)
        ),

    MakeBeat("Calls father's business. Tries to asks questions but is awkward.")
        .if_not(fathers_secretary_left_on_vacation)
        .ok_if(caseOfMissingFather(1), isAwkward(1))
        .sets_up(was_awkward_to_fathers_secretary),

    MakeBeat("""If PI has a dead brother, establish that PI and brother shared
            everything and helped each other out when they were poor. Just
            before he died they had an argument where brother accused PI of
            drifting away because he had made some money and new friends. PI
            always regretted not saying the right thing in that moment.""")
        .ok_if(hasDeadBrother(0), isPI(0))
        .sets_up(theme_of_money_conflict_between_siblings),

    MakeBeat("""Client's father has an older estranged brother who PI goes and
            speaks to even though client says not to. Father's older brother
            tells PI stories about client's father that give PI leads to
            investigate stuff.""")
        .if_not(is_clients_father_brother(any1))
        .ok_if(is_character(1))
        .sets_up(
            is_clients_father_brother(1),
            theme_of_money_conflict_between_siblings
        ),

    MakeBeat("""At the end turns out client's father's older brother who is poor
            killed the father because he never shared his wealth and older
            brother thought he was owed it for raising client's father (as their
            parents had died""")
        .ok_if(is_clients_father_brother(1), HerosJourney.find)
        .sets_up(foundMotive, isPerp(1)),

    # TODO: if PI's ghost is a fear of placeA, final showdown should be at
    # placeA

    # TODO: if antagonist has pretended to be someone else, final showdown in
    # house of mirrors

    MakeBeat("Client saw PI in a dream")
        .ok_if(isPI(0), isClient(1), now_at(0, 2), now_at(1, 2), HerosJourney.take)
        .express(actions.say_saw_pi_in_a_dream, {"pi": 0, "client": 1})
        .sets_up(trusts(1, 0)),

    MakeBeat("Finally realizes money from victim to x was because they were " +
        "friends and victim was doing x a favor, which the PI couldn't " +
        "understand before because they assumed everyone is selfish. " +
        "Therefore x was lying about the money being for a business " +
        "arrangement and they did not personally know each other, so x is " +
        "very likely the perp or is in on it.")
        .ok_if(isCocky(1), learned_to_enjoy_empathy(1))
        .sets_up(foundEvidenceOfPerp(1,2), HerosJourney.take),

    MakeBeat("""Was able to call secretary up where their conversation earlier
        in the story was super awkward. PI apologizes and plays it off like
        they were super tired or upset that day and then the secretary accepts
        their apology and demonstration of not being so awkward and helps the
        PI out by saying that the father met with PI's mentor the day he
        disappeared.""")
        .ok_if(
            learned_to_apologize_and_recover_from_mistakes(1),
            was_awkward_to_fathers_secretary,
            hasGuidance(1, 2)
        )
        .if_not(foundEvidenceOfPerp(1, any1))
        .sets_up(foundEvidenceOfPerp(1, 2), isPerp(2), HerosJourney.take),

    MakeBeat("Halucinate confession. Thinks it's real. Accuses the person " +
        "when waking up but then finds out it was just a fever dream. Is " +
        "forced to appologize.")
        .ok_if(isPI(0), is_injured_in_hospital(0), isCocky(0))
        .sets_up(made_a_huge_faux_pas(0)),

    MakeBeat("1 breaks into car. Takes out a big ring of keys and tries each " +
        "one by one. Looking calmly straight ahead the whole time.")
        .ok_if(is_gangster(1))
        .sets_up(stole_car(1)),

    MakeBeat("Awkward protag is framed for murder so must call date who " +
        "rejected them to clear themself")
        #TODO: express call date on phone
        .express(actions.ask_how_are_you, {"person": 1})
        .express(
            actions.say_they_are_happy_just_being_alive_cooly, {"person": 2}
        )
        #TODO: express explain situation awkwardly 
        #TODO: express date helps 1 out
        .ok_if(went_on_a_date_with(1,2), is_framed(1), isAwkward(1))
        .sets_up(must_call_for_alibi(1,2)),
]

beats = (
    conversations.beats + plot.beats + character_arc.beats + high_level_beats
)

high_level_logic_rules = [
    MakeLogic("Both arc and plot must cross threshold together.")
        .ok_if(HerosJourneyPlot.go, HerosJourneyCharacterArc.go)
        .sets_up(HerosJourney.go)

    MakeLogic("Any case means has a case.")
        .ok_if(caseOfMissingFather(0))
        .ok_if(father_being_shady_case, isPI(0))
        .sets_up(hasACase(0)),

    MakeLogic("Made a faux pas.")
        .ok_if(made_incorrect_public_accusation(0))
        .sets_up(made_a_huge_faux_pas(0)),
]

logic_rules = character_arc.logic + high_level_logic_rules

# A theory for cycles in the story:
#
# The situations the characters end up in are based on the theme / tone at that
# point. For exmaple if characters are far from home they can encounter a road
# that is broken and overgrown.
#
# Things happen to the characters based on the situations they are in. For
# example, one character may trip on the broken pavement.
#
# Characters can take action in response to things happening to them or their
# friends for example one character may go help their friend who tripped get
# back up.
#
# Actions move a character on their arc and change the theme / tone appropriate
# for that point in their arc. For example if characters have demonstrated that
# they care about each other / have each others back, they will encounter can
# encounter a high wall that they have to boost / pull each other up.
#
# If some kind of lost characters just climbed up a big wall, they can look
#  out and see where they are going and no longer feel lost.

# A theory for cycles in the story:
# 1. Conflict occurs
# 2. Address physical consequences
# 3. Confront internal consequences
# 4. Accept new reality

# TODO: if it feels like pacing is bad and story is losing steam. Consider using
# the scene_can_end concept to require all scenes to add a new wrinkle to the
# mystery / challenge an assuption / turn the case on it's head / etc.

# TODO: can we somehow limit the number of plot threads? Would make sense to
# limit it to 2 or 3 so the story doesn't get too complicated and difficult to
# end.

content_pack = ContentPack(
    objects,
    pre_established_concepts,
    beats,
    logic_rules,
    object_expressions
)

# TODO: For alcoholic, has to keep reminding himself to be a real person. That
# the alcoholic is just a zombie. The thoughts pop into his head. When he gets
# frustrated he thinks having a drink will clear his head. When he succeeds he
# thinks he should have a drink to celebrate.

#TODO: scene where character writes a letter that noone will ever read (they
#assume), or makes a recording noone will ever hear.

#TODO: if character is a gangster, daughter forms relationship with friend, then
# is forced to whack friend. Daughter can tell character did it or at least
# is on the same side as those who did. Never speaks to character again.

#TODO: perspective espoused by character: all human tragedy comes from
# the difference in size between the sexes. What actions does that lead this
# character to take?

# TODO: character arc for a side character: He spends his whole life taking care
# of a house and then realizes he doesn't have to. Decides to leave and try
# other kinds of work. Fits the theme of why we feel duty or obligation to stay
# where we are / keep doing what we've been doing. Like the sunken cost fallacy
# for life choices.
#  -  Another telling of a similar arc: a character wanted to do good things as
# a child, be true to oneself. Had to take a job to survive. Struggled to figure
# out what to do with life. Had a habit of falling into working hard and getting
# better at work because it's easier. Woke up one day and realized they were
# struggling so hard to do something didn't really care about.
#  -  The PIs need to look info what happened during an old legal case involving
# the missing father so they track down his attorney.
# "You used to work with X at the law firm. Everyone we talked to says you were
# the best laywer they had. You would have made partner if you had stayed on for
# another six months. Why did you leave?"
# "I kept asking myself, why are you here? I gave a shit for a while. I did. I
# worked hard cause I thought we were doing good work. That's why they all
# thought I was a good lawyer. But the partners didn't care. The old guys. They
# were a revolving door anyways. Hard to know your department head's vision when
# they change every 3 years. People were quitting and they didn't backfill. Case
# load piled up and we worked hard cause we cared and thought they would find
# someone as soon as they could. But they didn't. They didn't care. Clients
# dropped us cause they got lost in the shuffle. But it didn't matter. The firm
# was so big it can't die. SOme junior lawyer will join up and some client will
# sign on based on the name. Nobody remembers what they did five years ago. So
# why did I give so many years to them? I don't know. I couldn't remember. So I
# left."
#  -  "I just woke up one day and couldn't remember why I cared. Why I was
# working so hard. So I left."

# TODO: case of missing radio personality. They assume she was killed by
# an obsessive fan. At the end, turns out she ended show on purpose because she
# realized it hurt people by creating parasocial relationships.

# TODO: some options for the protagonist being a bad guy. Can have l'etranger
# ending where they find purpose in being hated. That's definitely a good option
# if player chooses to have protagonist just kille everyone. Can be like Millers
# Crossing or The Irishman where they have no connections to anyone in the end.
# Can do a cool "what heart" reveal moment that the protag is bad like in
# Miller's Crossing.

# TODO: word bank of mishearings to create mysteries based on that

# TODO: bad guy alters the deal. Best bet he doesn't alter it further.

# TODO: grifter character: when someone smart questions them, they charm the
# smart person by highlighting their intelligence. They pretend to pull them
# into their inner circle.
