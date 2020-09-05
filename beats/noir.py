from story import (
    Concept,
    ContentPack,
    MakeBeat,
    MakeLogic,
    NarrativePiece,
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

# Cases
caseOfMissingFather = Concept(1, "missingFather")
father_being_shady_case = Concept(0, "caseOfShadyFather")

asked_how_was_your_father = Concept(0)
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
is_fathers_secretary = Concept(1)
is_framed = Concept(1)
is_in_satanic_cult = Concept(1)
is_injured_in_hospital = Concept(1)
lives_with = Concept(2, "livesWith")
run_off_together = Concept(2)
stole_car = Concept(1)
thinks_father_wanted_to_leave_family = Concept(0)
trusts = Concept(2) # 1st trusts 2nd
wants_to_see_something_happen_tomorrow_morning = Concept(1)
went_on_a_date_with = Concept(2)
wore_a_blue_rose = Concept(1)
writhed_on_the_ground = Concept(1)

doesnt_take_client_seriously = Concept(0)
# 1st parameter is the detective, 2nd is mentor
hasGuidance = Concept(2, "hasGuidance")
started_talking = Concept(2)
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

# Backstories (a.k.a The Ghost):
# A good backstory is when characters blame themselves for something bad, as
# they must have character growth to overcome it.
isFormerCop = Concept(1, "isFormerCop")
isFormerOpiumAdict = Concept(1, "isFormerOpiumAdict")
hasDeadBrother = Concept(1, "deadBro")
wifeDiedRandomly = Concept(1, "wifeDiedRandomly")

# Begin Character Arcs ==========================

# Awkward arc:
learned_to_appologize_and_recover_from_mistakes = Concept(1) # need
thinks_making_a_social_mistake_is_unforgivable = Concept(1) # lie
wants_to_be_in_proximity_of_someone_they_fancy = Concept(1) # want
saw_has_no_wedding_ring_on = Concept(2) # (+ is_attracted_to) lock-in
made_a_huge_faux_pas = Concept(1) # lowest point
#(TODO: example: he appologizes and offers to resign from case. But what's a
# reason for him to stay on that doesn't seem cheap?
sincerely_applogized = Concept(1) # sacrifice-action
is_comfortable_around_those_attracted_to = Concept(1) # ultimate boon
made_a_platonic_friend = Concept(1) # ultimate boon

# Cocky arc
learned_to_enjoy_empathy = Concept(1) # (understands will receive it back) need
thinks_being_selfish_is_always_ok = Concept(1) # lie
wants_to_have_hedonistic_fun_and_not_care_about_others = Concept(1) # want
thinks_this_case_can_prove_how_good_of_pi_they_are = Concept(1) # lock-in
#TODO: make a socail faux pas with brashness, almost ruin case # lowest point
# This should subvert the trope of detectives being generally able to get away
# with breaking social boundaries due to that title.
was_forced_to_empathize_with_someone_to_get_info = Concept(1) # sacrifice-action
made_a_true_friend = Concept(1) # ultimate boon

# Can't be intimate arc
learned_love_is_worth_it_even_if_you_get_hurt = Concept(1) #need
thinks_needs_to_protect_self_from_intimacy = Concept(1) #lie
wants_to_work_hard_to_distract_from_personal_life = Concept(1) #want
#TODO: lock-in
#TODO: lowest point
#TODO: sacrifice-action
#TODO: boon

# Understand mortality arc
learned_to_see_how_the_cycle_life_and_death_shapes_the_world = Concept(1) # need
thinks_that_life_is_blissfully_unchainging = Concept(1) # lie
feels_cannot_relate_to_others_and_wants_to = Concept(1) # want
#TODO # lock-in
#TODO: forced to face their own mortality # lowest point
# (finally quits after always saying they could any time)
quit_smoking = Concept(1) # sacrifice-action
finally_heard_the_lyrics_of_fleeting_love_in_karaoke_song = Concept(1) # boon

# Start pacificst arc
learned_that_there_are_no_absolutes = Concept(1) # need
thinks_there_is_absolute_morality = Concept(1) # lie
wants_to_prove_pacificism_is_right = Concept(1) # want
#TODO # lock-in
#TODO: some situation where using violence earlier would have helped # lowpoint
killed_to_prevent_a_mob_war = Concept(1) # sacrifice-action
spiraled_into_alchoholism = Concept(1) # boon (negative arc)

# Becomes content nihilist arc
became_content_with_meaninglessness_of_life = Concept(1) # need
thinks_needs_to_find_secret_purpose_to_start_living = Concept(1) # lie
wants_to_find_deeper_meaning_in_life = Concept(1) # want
# A typical aspect of this problem is focus on novelty. Novel ideas seem like
# they are a deeper purpose but then turn out to not be, and it gets harder and
# harder to find new things as life goes on. So in this example the protagonist
# finds out that the missing father is trying to reform the political system
# with rank choice voting that the protagonist has never heard of before.
heard_person_is_head_of_group_fighting_for_irv = Concept(2) #lock-in
learned_irv_will_not_solve_all_problems = Concept(1) #lowest-point
#TODO: sacrifice-action
empathized_with_others_struggling_to_accept_life_is_meaningless = Concept(1)#bn

# Get over life expectations arc
learned_to_not_miss_what_they_were_never_entitled_to = Concept(1) #need
# A consequence of this is that they can't conncentrate on the case as they keep
# thinking about past mistakes and regrets.
thinks_they_cant_be_happy_if_their_life_hasnt_progressed_as_they_expected = (
    Concept(1)
) #lie
wants_to_have_a_family_and_good_job_by_now = Concept(1) #want
#TODO: lock-in
#TODO: lowest-point
didnt_hit_on_new_coworker_as_she_clearly_is_attracted_to_other_coworker = (
    Concept(1)
) #sacrifice-action
can_truly_concentrate_on_the_case = Concept(1) #boon
# made_a_true_friend - boon

# Obsessive arc
#TODO: need
#TODO: lie
#TODO: want
#TODO: lock-in
# lowest-point
are_still_looking_for_father_long_after_client_accepted_he_is_dead = Concept(1)
doesnt_notice_child_aged_five_years = Concept(1) # lowest-point
# e.g. "I'll just work at the fucking hardware store".
quit_being_pi_for_simple_life = Concept(1) # sacrifice-action
# TODO: boon

# Dirty cop arc
#TODO: need
#TODO: lie
#TODO: want
#TODO: lock-in
other_cop_died_because_of_info_protag_gave_mob_boss = Concept(1) #lowest-point
betrayed_and_killed_mob_boss = Concept(1) # sacrifice-action
# spiraled_into_alchoholism - boon (negative arc)

# Behind the times arc
learned_how_people_act_in_modern_times = Concept(1) #need
# The client and her father should both have this lie
assumes_business_is_still_conducted_in_the_old_ways = Concept(1) #lie
#TODO: want
#TODO: lock-in
#TODO: lowest-point
#TODO: sacrifice-action
can_finally_see_who_obviously_kidnapped_her_father = Concept(1) #boon
now_know_how_to_save_the_company = Concept(1) #boon

# Disgraced former cop arc
learned_to_be_content_following_own_principles = Concept(1) #need
ties_self_esteem_to_acceptance_by_an_organization = Concept(1) #lie
wants_to_prove_themself_as_loyal = Concept(1) #want
pis_boss_says_case_is_important = Concept(1) #lock-in
pis_boss_undermines_the_investigation = Concept(1) #lowest-point
disobeyed_a_direct_order = Concept(1) #sacrifice-action
# TODO: boon

# Antisocial arc
learned_to_stay_calm_in_social_situations = Concept(1) #need
thinks_they_need_to_lash_out_when_they_feel_uncomforable = Concept(1) #lie
#TODO: want
#TODO: lock-in
#TODO: lowest-point
#TODO: sacrifice-action
#TODO: boon

# Creepy arc
#TODO: need
thinks_making_others_uncomfortable_has_no_consequence = Concept(1) #lie
#TODO: want
#TODO: lock-in
#TODO: lowest-point
#TODO: sacrifice-action
#TODO: boon

# End Character Arcs ==========================

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

narrative_pieces = ([
    # TODO: I really need a robust system of mutually exclusive concepts or just
    # derived concepts. Like I don't want to establish a character as a PI if
    # they already have a profession. Similarly I don't want to establish a new
    # case if they already have a case. Currently we have the "hasACase" thing
    # but it's silly to have to remember to establish that alongside the actual
    # case concept every time. One alternative, is that parameters to concepts
    # paired with "any" checks act like mutual exclusivity. So I could have
    # professions become objects and also the cases become objects.
    MakeBeat("Introduce PI in office")
        # Need to establish protagonist before this phase is done
        .if_not(HerosJourney.you)
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
        .ok_if(now_at(1, pet_shop))
        .sets_up(scene_can_end),

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
        .sets_up(talking_on_phone(1, 2), talking_to(1, 2)),

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
            talking_on_phone(1, nobody)
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
        .sets_up(isCocky(1)),

    MakeBeat("Introduce Ramen shop owner")
        .express(descriptions.opened_shop_late_at_night, {"person": 1})
        .express(descriptions.served_late_night_customers, {"person": 1})
        # Need to establish protagonist before this phase is done
        .if_not(HerosJourney.you)
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

    MakeBeat("Rejects empathy attempt from coworker")
        .ok_if(isProtag(0), isPI(0), now_at(0, pi_office))
        .ok_if(isProtag(0), isRamenShopOwner(0), now_at(0, ramen_shop))
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

    MakeBeat("Client walks in")
        .express(actions.see_client_walk_in, {"pi": 0, "client": 1})
        .if_not(now_at(any1, pi_office), isClient(any1)) # for any other char
        .if_not(hasACase(0))
        .if_not(knows_is_creepy(1, 0))
        .if_not(kickedOutClient(0, 1))
        .ok_if(isPI(0), now_at(0, pi_office), are_different(0, 1))
        .sets_up(now_at(1, pi_office), isClient(1)),

    MakeBeat("Hang up because see client")
        .express(actions.hang_up, {"person": 0})
        .ok_if(now_at(1, pi_office), isClient(1), talking_on_phone(0, 1))
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
            HerosJourney.go,
            scene_can_end
        ),

    MakeBeat("Notices has no wedding ring on")
        .ok_if(isAwkward(1), now_at(1, 3), now_at(2, 3), are_different(1, 2))
        .sets_up(saw_has_no_wedding_ring_on(1, 2), is_attracted_to(1, 2)),

    MakeBeat("Closes shop and leaves.")
        .express(actions.close_ramen_shop, {"owner": 0})
        .ok_if(isRamenShopOwner(0), now_at(0, ramen_shop), scene_can_end)
        .sets_up(now_at(0, the_streets)),

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

    #TODO: somehow have leaving the office possibly lead to walking home or cut
    # straight to being home

    MakeBeat("#0 Walks home in the rain. Sees shadows of people following them.")
        .express(actions.walk_to, {"person": 0, "to": pi_home}, modifiers.in_rain)
        .express(actions.see_shadows_of_people_following, {"person": 0})
        .ok_if(isProtag(0), now_at(0, unknown_location))
        .sets_up(isParanoid(0), now_at(0, the_streets)),

    MakeBeat("Goes home.")
        .express(actions.go_home, { "person": 0})
        .express(descriptions.pi_at_home, { "pi": 0})
        .ok_if(isProtag(0), now_at(0, the_streets))
        .sets_up(now_at(0, pi_home)),

    MakeBeat("Avoids talking to mom.")
        .ok_if(
            isProtag(0),
            now_at(0, pi_home),
            is_character(1),
            are_different(0, 1)
        )
        .if_not(is_mother_of(any1, 0), are_different(1, any1))
        .express(actions.avoid_interaction_with_mother, {"pi": 0, "mother": 1})
        .sets_up(isAwkward(0), lives_with(0, 1), is_mother_of(1, 0)),

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
        .if_not(talking_on_phone(0, any1), are_different(any1, nobody))
        .if_not(asked_how_was_your_father)
        .express(actions.say_met_client_and_father_once_and_admire_father, {"pi": 0, "client": 1})
        .sets_up(asked_how_was_your_father),

    MakeBeat("Father missing case")
        .ok_if(
            isPI(0),
            now_at(0, pi_office),
            isClient(1),
            now_at(1, pi_office),
            asked_how_was_your_father,
        )
        .if_not(hasACase(0))
        .express(actions.hear_client_father_is_missing, {"pi": 0, "client": 1})
        .sets_up(caseOfMissingFather(0), HerosJourney.need),

    MakeBeat("Is very eager to take case")
        .ok_if(
            hasACase(0),
            now_at(0, pi_office),
            isClient(1),
            now_at(1, pi_office),
            thinks_needs_to_protect_self_from_intimacy(0)
        )
        .sets_up(wants_to_work_hard_to_distract_from_personal_life(0)),

    MakeBeat("Sister ran off case")
        .ok_if(
            isPI(0),
            now_at(0, pi_office),
            isClient(1),
            now_at(1, pi_office),
            asked_how_was_your_father
        )
        .if_not(hasACase(0))
        .express(actions.hear_daughter_has_run_off, {"pi": 0, "client": 1})
        .sets_up(hasACase(0), HerosJourney.need),

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
            asked_how_was_your_father
        )
        .if_not(hasACase(0))
        .sets_up(hasACase(0), HerosJourney.need),

    MakeBeat(
        "Client gives PI a fake identity and has them eavesdrop on father at " +
        "fancy party."
    )
        .ok_if(
            isPI(1),
            father_being_shady_case,
        )
        .if_not(knows_to_check_out_docks(1))
        .sets_up(knows_to_check_out_docks(1)),

    # TODO: ask client when they last saw father, they say the morning before,
    # he left for work but never arrived at the office. Later it turns out
    # client had been staying with her bf for a few days so hasn't actually
    # seen father for several days, but she kept that a secret because she's
    # supposed to be engaged to someone else.
    #
    # This is a general formula: encounter another person connected to the case
    # maid,
    # secretary,
    # brother,
    # policeman,
    # etc.
    # Then it turns out that that character lied, which seems suspicious, but
    # it turns out they lied for some other reason (they don't want a scandal
    # to get out, they are commiting another crime and want to hide it, they
    # are in denial) except for the last one at the end of the story who does
    # turn out to be the perp.

    MakeBeat("Look in study")
        .ok_if(
            isPI(0),
            now_at(0, client_home),
            isClient(1),
            now_at(1, client_home),
            caseOfMissingFather(0)
        )
        .express(actions.look_in_study, {"pi": 0, "client": 1})
        .sets_up(client_is_hiding_something),

    # This seems like he wanted to leave his family but really he just wanted
    # to do the dishes.
    MakeBeat("Finds wedding ring and watch on counter")
        .ok_if(
            isPI(0),
            now_at(0, client_home),
            caseOfMissingFather(0)
        )
        .express(actions.find_wedding_ring_and_watch_on_counter, {"pi": 0})
        .sets_up(thinks_father_wanted_to_leave_family),

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

    # Hooks
    MakeBeat("Victim was killed with gun in safe that only victim and " +
        "daughter knew the combination to")
        #TODO
        .sets_up(),

    MakeBeat("PI has partner who goes out first to tail the guy. Get's " +
        "killed. PI's ghost is that he was sleeping with partner's wife.")
        #TODO
        .sets_up(),

    # End hooks

    MakeBeat("Takes gun out of desk")
        .express(actions.take_gun_out_of_desk, {"person": 0})
        .ok_if(now_at(0, pi_office), isProtag(0))
        #TODO: should use some special concepts to say anbody not the PI rather
        # than just checking against the client
        .if_not(now_at(any1, pi_office), isClient(any1))
        .sets_up(has_a_gun(0)),

    #TODO: Character arc for awkward pi:
    # -  he talks about how his grandfather built a house when he was 25. Ends
    #    up not being a very good PI and client does most of the work to solve
    #    case. protag quits being a PI and becomes a carpenter or construction
    #    worker.

    MakeBeat("Wakes up disheveled. Asks dog to find keys while getting dressed.")
        .ok_if(now_at(0, pi_home), isCreepy(0))
        .ok_if(now_at(0, pi_home), isObsessive(0))
        .sets_up(asked_dog_to_find_keys, scene_cannot_end),

    MakeBeat("Has to find keys because dog obviously can't.")
        .ok_if(asked_dog_to_find_keys)
        .if_not(found_keys)
        .sets_up(scene_can_end, found_keys),

    MakeBeat("Dog can actually find keys.")
        .if_not(serious_tone)
        .if_not(found_keys)
        .ok_if(asked_dog_to_find_keys, now_at(0, pi_home), isPI(0))
        .sets_up(dogCanFindKeys, found_keys, silly_tone, scene_can_end),

    MakeBeat("Someone robbed Protag")
        .ok_if(isProtag(0), now_at(0, pi_home))
        .sets_up(protagGotRobbed),

    MakeBeat("Tries to buy drugs from a dude while his dad is there and then "
        + "he comes over and chews protag out.")
        .ok_if(told_to_go_smoke_weed, isProtag(0))
        .sets_up(made_a_huge_faux_pas(0)),

    MakeBeat("Makes incorrect accusation unnecessarily publicly and confidently")
        .ok_if(isAwkward(0), HerosJourney.search)
        .ok_if(isCocky(0), HerosJourney.search)
        .if_not(talking_on_phone(0, any1))
        .sets_up(made_a_huge_faux_pas(0), HerosJourney.find),

    MakeBeat("PI slept and dreamed of heroin.")
        .if_not(ProtagonistDefinition.ghost)
        .ok_if(isPI(0), now_at(0, pi_home))
        .sets_up(isFormerOpiumAdict(0), ProtagonistDefinition.ghost),

    MakeBeat("Finds match book from burglars")
        .ok_if(protagGotRobbed)
        .sets_up(burglarsHungOutAtBar()),

    MakeBeat("Has big conspiracy board with yarn and stuff")
        .if_not(hasGuidance(0, any1))
        .ok_if(now_at(0, pi_office), isProtag(0), hasACase(0), HerosJourney.go)
        .sets_up(isObsessive(0)),

    MakeBeat("Gets books. Hunkers down. Studies")
        # TODO: there needs to be some mystery in the case that the protag can
        # use scientific knowledge to work out. The beat should be gated on that
        # and then set up that the protag has figured out the case by the
        # knowledge making them suddenly realize something.
        .ok_if(isProtag(0), feels_motivated(0), HerosJourney.find)
        .sets_up(),

    MakeBeat("Goes to missing father's office. Interviews secretary who is "
        "wearing a blue rose on her lapel.")
        .ok_if(caseOfMissingFather(0), is_fathers_secretary(1), scene_can_end)
        .sets_up(wore_a_blue_rose(1)),

    MakeBeat("Asks old boss for help")
        # This beat is a whole scene
        #
        # TODO: express that he is asking for help because he has never done a
        # disappearance/murder before and this is really hard compared to dumb
        # cheating cases.
        # TODO: boss must give some advice as if it's relating to a common thing
        # but really it's very unusual that the father had this thing. This was a
        # deliberate diversionary tactic by old boss.
        # TODO: boss must use a metaphor that turns out to be a little too
        # literal later on, implying the boss had seen the crime scene.
        .ok_if(
            scene_can_end,
            hasACase(1),
            are_different(1, 2),
            HerosJourney.need
        )
        .if_not(isClient(2))
        .if_not(hasGuidance(1, any1))
        .sets_up(started_talking(1, 2), is_old_boss(2), scene_cannot_end),

    MakeBeat("Old boss suggests smoking weed to think about case with a "
        + "broadened perspective")
        .ok_if(talking_to(1, 2), is_old_boss(2))
        .sets_up(told_to_go_smoke_weed),

    MakeBeat("Finishes talking to old boss")
        .ok_if(talking_to(1, 2), is_old_boss(2))
        .sets_up(hasGuidance(1, 2), talking_to(1, nobody), scene_can_end),

    MakeBeat("Second client comes in, sounds like they're also involved in " +
        "the case. Then when the secretary goes home the fake client pulls a gun.")
        # gate on 'go' because this shouldn't happen in act 1
        .ok_if(
            isPI(1),
            now_at(1, pi_office),
            is_character(2),
            are_different(1, 2),
            HerosJourney.go
        )
        .if_not(isClient(2))
        .sets_up(has_a_gun(2)),

    MakeBeat("Sleeps with someone he just met. Sneaks out in the morning for " +
        "good reason related to case (expecting to catch someone at a certain" +
        " time or keeping a planned meeting). Later girl calls him and asks " +
        "if he knows how it amde her feel to wake up alone")
        .ok_if(
            isProtag(1),
            are_attracted_to_each_other(1,2),
            has_appointment_tomorrow_morning(1)
        )
        .ok_if(
            isProtag(1),
            are_attracted_to_each_other(1,2),
            wants_to_see_something_happen_tomorrow_morning(1)
        )
        .sets_up(is_inconsiderate(1)),

    MakeBeat("Breaks into father's appartment.")
        .ok_if(isObsessive(1), caseOfMissingFather(1))
        .ok_if(hasGuidance(1,2), caseOfMissingFather(1))
        .sets_up(inFathersAppartment(1)),

    MakeBeat("Finds father dead.")
        .if_not(silly_tone)
        .ok_if(inFathersAppartment(1))
        .sets_up(serious_tone, foundDeadFather(1), HerosJourney.go),

    MakeBeat("Finds match book on father's body.")
        .ok_if(foundDeadFather(0), HerosJourney.go)
        .sets_up(fatherHungOutAtBar()),

    MakeBeat("Finds paper with non-sensical phrases.")
        .ok_if(foundDeadFather(0), HerosJourney.go)
        .sets_up(heardCodedWords),

    #TODO: erg what should we do if the protag has been to the bar before cause
    # of burglars and matchbook
    MakeBeat("Sees missing father on street and follows to seedy bar")
        .ok_if(isRamenShopOwner(0), now_at(0, the_streets))
        .if_not(saw_missing_father_head_to_bar)
        .sets_up(now_at(0, bar), saw_missing_father_head_to_bar),

    MakeBeat("Goes to seedy bar.")
        .express(
            actions.enters_seedy_bar,
            {"pi": 0, "doorman": 1},
            unnamed={"doorman": nouns.doorman}
        )
        .ok_if(fatherHungOutAtBar(), isProtag(0), is_character(1))
        .ok_if(burglarsHungOutAtBar(), isProtag(0), is_character(1))
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
        .ok_if(isAwkward(1), now_at(1, pi_office))
        .if_not(now_at(1, pi_home), lives_with(1, any1), is_mother_of(any1, 1))
        .if_not(talking_on_phone(1, any1))
        .sets_up(
            wants_to_have_a_family_and_good_job_by_now(1),
            thinks_they_cant_be_happy_if_their_life_hasnt_progressed_as_they_expected(1),
            thinks_needs_to_protect_self_from_intimacy(1)
        ),

    # TODO: this could also be a fortune teller, so not at the bar
    MakeBeat("Asks about match book and meets mysterious woman")
        .ok_if(
            now_at(0, bar),
            is_character(1),
            is_character(2),
            fatherHungOutAtBar
        )
        .ok_if(
            now_at(0, bar),
            is_character(1),
            is_character(2),
            burglarsHungOutAtBar
        )
        .express(
            actions.ask_about_match_book_then_meet_mysterious_woman,
            {"pi": 0, "bartender": 2, "ml": 1},
            unnamed={"bartender": nouns.bartender}
        )
        .express(actions.join_mysterious_woman, {"pi": 0})
        .sets_up(joined_mysterious_woman_at_booth),

    # TODO: this could also be a fortune teller, so not at the bar
    MakeBeat("Follows father inside and meets mysterious woman")
        .ok_if(
            now_at(0, bar),
            is_character(1),
            is_character(2),
            saw_missing_father_head_to_bar
        )
        .if_not(joined_mysterious_woman_at_booth)
        .express(
            actions.follow_father_inside_then_meet_mysterious_woman,
            {"pi": 0, "bartender": 2, "ml": 1},
            unnamed={"bartender": nouns.bartender}
        )
        .express(actions.join_mysterious_woman, {"pi": 0})
        .sets_up(joined_mysterious_woman_at_booth, talking_to(0, 1)),

    # TODO: this could also be a fortune teller, so not at the bar
    MakeBeat("Talks to mysterious woman.")
        .ok_if(now_at(0, bar), joined_mysterious_woman_at_booth)
        .sets_up(talkedToMysteriousWoman),

    # sets up for character change at the end, this is needed to accept
    # that the mentor was a bad guy
    MakeBeat("Mystery woman says client's father betrayed his own brother and "
        + "you have to accept loss.")
        .ok_if(
            now_at(1, bar),
            hasDeadBrother(1),
            talkedToMysteriousWoman,
            caseOfMissingFather(1)
        )
        .if_not(HerosJourney.search)
        .sets_up(HerosJourney.search, talking_to(1, nobody)),

    # sets up for character change
    MakeBeat("Mystery woman says dead father had no faith but you have to have faith.")
        .ok_if(
            now_at(1, bar),
            wifeDiedRandomly(1),
            talkedToMysteriousWoman,
            caseOfMissingFather(1)
        )
        .if_not(HerosJourney.search)
        .sets_up(HerosJourney.search, talking_to(1, nobody)),

    # sets up for character change
    MakeBeat("Mystery woman says you are living too much in where people " +
        "could be. Focus on where they are now.")
        .ok_if(now_at(1, bar), isFormerCop(1), talkedToMysteriousWoman)
        .if_not(HerosJourney.search)
        .sets_up(
            told_to_focus_on_where_people_are,
            HerosJourney.search,
            talking_to(1, nobody)
        ),

    MakeBeat("Mystery woman says you are not a real person. You're just " +
        "someone else's dream.")
        .ok_if(now_at(1, bar), talkedToMysteriousWoman)
        .if_not(HerosJourney.search)
        .sets_up(
            we_live_inside_a_dream,
            HerosJourney.search,
            talking_to(1, nobody)
        ),

    MakeBeat("Leaves seedy bar.")
        .ok_if(HerosJourney.search, now_at(0, bar))
        .sets_up(now_at(0, the_streets)),

    MakeBeat("Calls father's business. Asks questions. Finds out father's " +
        "secretary started a month long vacation 1 week before father " +
        "disappeared.")
        .ok_if(told_to_focus_on_where_people_are, caseOfMissingFather(1))
        .sets_up(fathers_secretary_left_on_vacation),

    MakeBeat("Calls regular, says saw their father run into bar but lost him")
        .ok_if(
            now_at(0, pi_home),
            told_to_focus_on_where_people_are,
            saw_missing_father_head_to_bar,
            is_regular(1)
        )
        .sets_up(knows_father_went_to_bar(1)),

    MakeBeat("Goes back to bar but it burned down")
        .if_not(now_at(1, bar))
        .if_not(bar_burned_down)
        #TODO: somehow have a way to track if has visited locations before, and
        # gate on that instead of the two other reasons specifically
        .ok_if(
            isProtag(1),
            HerosJourney.find,
            burglarsHungOutAtBar,
            fatherHungOutAtBar,
        )
        .ok_if(
            isProtag(1),
            HerosJourney.find,
            burglarsHungOutAtBar,
            saw_missing_father_head_to_bar
        )
        .sets_up(bar_burned_down, now_at(1, bar)),

    MakeBeat(
        "PI asks bar neighbor why it burned down. Gets hint to go to docks."
    )
        .express(
            actions.ask_why_bar_burned_down,
            {"pi": 1, "bystander": 2},
            unnamed={"bystander": nouns.neighbor}
        )
        .express(descriptions.knows_fish_company_by_docks, {"pi": 1})
        .ok_if(isPI(1), bar_burned_down, is_character(2))
        .sets_up(HerosJourney.find, knows_to_check_out_docks(1)),

    # TODO: follow up with watching them perform a ritual that fails.
    # TODO: if supernatural established then maybe could be real
    MakeBeat("Finds out that dead father was in satanic cult.")
        # Require PI is obsessive for thematic reasons
        .ok_if(HerosJourney.find, isObsessive(1), caseOfMissingFather(1))
        .sets_up(foundMotive, satanicCult),

    MakeBeat("Protag finds satanic cult hideout with blue rose as the symbol.")
        .ok_if(wore_a_blue_rose(0), satanicCult)
        .sets_up(is_in_satanic_cult(0)),

    MakeBeat("Overhears that dead father was involved in scandal.")
        .ok_if(HerosJourney.find, politicalScandal, caseOfMissingFather(1))
        .sets_up(foundMotive),

    MakeBeat("Finds evidence criminal mastermind did it.")
        .ok_if(foundMotive, isObsessive(1), are_different(1, 2))
        .sets_up(foundEvidenceOfPerp(1,2), isPerp(2), HerosJourney.take),

    MakeBeat("Dog finds keys to free PI.")
        .ok_if(isChainedUp(0), isPI(0), dogCanFindKeys)
        .sets_up(isFree(0)),

    MakeBeat("Writhes on ground from awkwardness.")
        .express(actions.writhe_on_ground, {"person": 0})
        .ok_if(
            now_at(0, pi_home),
            isAwkward(0),
            was_in_traumatic_awkward_situation(0)
        )
        .ok_if(
            now_at(0, pi_home),
            isAwkward(0),
            made_a_huge_faux_pas(0)
        )
        .if_not(writhed_on_the_ground(0))
        .sets_up(
            now_at(0, pi_home),
            thinks_making_a_social_mistake_is_unforgivable(0),
            writhed_on_the_ground(0)
        ),

    # TODO: need to expand on this
    MakeBeat("Finds evidence his old boss did it.")
        .ok_if(foundMotive, hasGuidance(1,2))
        .sets_up(foundEvidenceOfPerp(1,2), isPerp(2), HerosJourney.take),

    MakeBeat("""Old boss did it because victim was going to screw the town over
            by forging documents saying that he owned some desert land that was
            about to be irrigated, just like the victim had done once before
            long ago to say that a gold mine was on their land instead of public
            land.""")
        .ok_if(hasGuidance(1,2), isPerp(2), politicalScandal)
        .sets_up(foundMotive),

    MakeBeat("""Old boss did it because he was a crooked PI who partnered with
            the victim and would steer the investiagation away from crooks who
            payed him off. Victim goes back to a cold case years later and won't
            drop it so old boss had to kill him.""")
        .ok_if(hasGuidance(1,2), isPerp(2), isPI(3), is_victim(3))
        .sets_up(foundMotive),

    MakeBeat("""Old boss did it because he was a mostly-straight PI but covered
            up for the crimes of his rich brother so that he would keep getting
            monetary gifts. The brother killed the victim accidentally,
            recklessly.""")
        .ok_if(hasGuidance(1,2), isPerp(2))
        .sets_up(foundMotive),

    MakeBeat("Turns out PI did it.")
        .ok_if(is_violent(0), is_psychopathic(0))
        .sets_up(foundEvidenceOfPerp(1,1), isPerp(1), HerosJourney.take),

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

    MakeBeat("""Was able to call someone up where their conversation earlier in
        the story was super awkward and the PI can apologize and play it off
        like they were super tired or upset that day and then afterwards the
        person accepts their apology and demonstration of not being so awkward
        and helps the PI out with some info.""")
        .ok_if(isAwkward(1), learned_to_appologize_and_recover_from_mistakes(1))
        .sets_up(foundEvidenceOfPerp(1,2), HerosJourney.take),

    MakeBeat("Goes to perps place.")
        .ok_if(foundEvidenceOfPerp(1,2), HerosJourney.take)
        .sets_up(now_at(1, perp_home), scene_cannot_end),

    MakeBeat("Perp sees PI and bolts.")
        .ok_if(now_at(0, perp_home), isPerp(1))
        .sets_up(runsAway(1)),

    MakeBeat("PI chases perp.")
        .ok_if(runsAway(1), now_at(2, perp_home))
        .sets_up(chasing(1, 2)),

    MakeBeat("PI is shot in shoulder by perp while running")
        .ok_if(chasing(1, 2), has_a_gun(2), isProtag(2))
        .sets_up(protagGotShot, HerosJourney.theReturn),

    MakeBeat("Frog 1 is here and I'm going to get him..")
        .ok_if(chasing(1, 2), isObsessive(2))
        .sets_up(story_end),

    MakeBeat("Perp gets cornered down an alley.")
        .if_not(isObsessive(2))
        .ok_if(chasing(1,2))
        .sets_up(cornered(1,2)),

    MakeBeat("Perp pulls a gun. Fires on our hero and misses. PI kills perp.")
        .ok_if(cornered(1, 2), has_a_gun(2))
        .sets_up(died(1), HerosJourney.take, scene_can_end),

    MakeBeat("Protag throws gun away")
        .ok_if(protagGotShot, has_a_gun(1), isProtag(1))
        .sets_up(has_no_gun(1)),

    MakeBeat("Client learns who kidnapped/killed father and thanks PI for closure")
        .ok_if(isPerp(1), gotArrested(1))
        .ok_if(isPerp(1), died(1))
        .sets_up(HerosJourney.theReturn),

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

    MakeBeat("Tunrs out father ran off for silly reason.")
        # Reason could be to free all captive horses in the state or something
        # TODO: express that he ran off with a younger woman to do the silly
        # thing because he wanted some excitement in his life.
        .ok_if(
            silly_tone,
            fathers_secretary_left_on_vacation,
            HerosJourney.take
        )
        .sets_up(HerosJourney.theReturn),

    #TODO: character change: learns that desires to kiss girlfriend on beach
    # aren't about any real person, just ideas from movies

    MakeBeat("Instead of going to look for missing father, stays home and " +
        "reads a book. Later gets a call from client/regular saying they need" +
        "to drive out to Indio. The car ride is long and quiet")
        .ok_if(
            we_live_inside_a_dream,
            caseOfMissingFather(0),
            isProtag(0),
            isClient(1)
        )
        .sets_up(now_at(0, the_streets), now_at(1, the_streets)),

    MakeBeat("Realizes coded message was telling him to go check out the " +
        "waterfront.")
        .ok_if(secretMessageSinger, isProtag(1))
        .sets_up(knows_to_check_out_docks(1)),

    MakeBeat("PI goes to the docks. Finds drug smuggling. Asks client about " +
        "it. Client initially plays if off but then admits she knew. PI asks " +
        "if she thinks that might be related to his disappearance. And why did"+
        " she not tell him. She says for obvious reasons she wants to keep it "+
        "on the DL. PI asks if she thought he wouldn't find out, angrily. He " +
        "is a PI after all.")
        .ok_if(knows_to_check_out_docks(1), isProtag(1))
        .sets_up(client_lied),

    MakeBeat("Finds secret society warehouse on the pier.")
        .ok_if(knows_to_check_out_docks(1), isProtag(1))
        .sets_up(HerosJourney.search),

    MakeBeat("Client's father was a member of a secret society. Society was "
        + "bringing in shipments of drug (not illegal, just unknown). PI "
        + "accidentally takes some. Runs off in delerium, seeing things.")
        .ok_if(
            HerosJourney.search,
            isProtag(0),
            caseOfMissingFather(0),
            knows_to_check_out_docks(0)
        )
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

    MakeBeat("Halucinate confession. Thinks it's real. Accuses the person " +
        "when waking up but then finds out it was just a fever dream. Is " +
        "forced to appologize.")
        .ok_if(isPI(0), is_injured_in_hospital(0), isCocky(0))
        .sets_up(made_a_huge_faux_pas(0)),

    MakeBeat("Amnesiac goes to jewler to ask about ring they are wearing. " +
        "Amnesiac said they found the ring. Jewler says, 'this is not " +
        "something you find, this is something you kill for. I want no part " +
        "of this.")
        .ok_if(is_amnesiac(0))
        .sets_up(),

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

    MakeBeat("Takes a risk and asks romantic interest to leave town with him")
        .ok_if(is_gambler(1), isProtag(1))
        .sets_up(run_off_together(1,2))
])

logic_rules = [
    MakeLogic("Any case means has a case.")
        .ok_if(caseOfMissingFather(0))
        .ok_if(father_being_shady_case, isPI(0))
        .sets_up(hasACase(0))
]

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
    narrative_pieces,
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
