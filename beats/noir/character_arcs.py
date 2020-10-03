from story import Concept, MakeAntiLogic, MakeBeat, MakeLogic, any1
from beats import core
from expression import actions
from expression import descriptions
from . import character_states
from . import inter_character_perceptions
from . import locations
from . import structure
from . import traits
from .nobody import nobody

# Backstories (a.k.a The Ghost):
# A good backstory is when characters blame themselves for something bad, as
# they must have character growth to overcome it.
isFormerCop = Concept(1, "isFormerCop")
isFormerOpiumAdict = Concept(1, "isFormerOpiumAdict")
# has a dead brother - has_dead_brother
wife_died_randomly = Concept(1, "wife_died_randomly")

# Awkward arc:
learned_to_apologize_and_recover_from_mistakes = Concept(1) # need
thinks_making_a_social_mistake_is_unforgivable = Concept(1) # lie
wants_to_be_in_proximity_of_someone_they_fancy = Concept(1) # want
saw_has_no_wedding_ring_on = Concept(2) # (+ is_attracted_to) lock-in
made_a_huge_faux_pas = Concept(1) # lowest point
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
#TODO: #need
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

class Hero:
    need = Concept(0)
    lie = Concept(0)
    want = Concept(0)
    lock_in = Concept(0)
    lowest_point = Concept(0)
    sacrifice_action = Concept(0)
    boon = Concept(0)

# General concepts only used in this file
writhed_on_the_ground = Concept(1)
regainFaith = Concept(1, "regainFaith")
run_off_together = Concept(2)

#TODO: character change: learns that desires to kiss girlfriend on beach
# aren't about any real person, just ideas from movies

#TODO: Character arc for awkward pi:
# -  he talks about how his grandfather built a house when he was 25. Ends
#    up not being a very good PI and client does most of the work to solve
#    case. protag quits being a PI and becomes a carpenter or construction
#    worker.

beats = [
    MakeBeat("Introduce dead brother")
        .if_not(traits.has_dead_brother(any1))
        .ok_if(
            traits.is_protag(0), thinks_needs_to_protect_self_from_intimacy(0)
        )
        .sets_up(traits.has_dead_brother(0)),

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
        .sets_up(isFormerCop(1)),

    MakeBeat("Rejects empathy attempt from coworker about dead brother")
        .express(
            actions.reject_empathy_attempt_about_brother,
            {"rejecter": 0, "empathizer": 1}
        )
        .ok_if(
            traits.is_protag(0),
            traits.is_pi(0),
            traits.has_dead_brother(0),
            core.now_at(0, locations.pi_office),
            core.is_character(1)
        )
        .ok_if(
            traits.is_protag(0),
            traits.is_ramen_shop_owner(0),
            traits.has_dead_brother(0),
            core.now_at(0, locations.ramen_shop),
            core.is_character(1)
        )
        .if_not(character_states.talking_on_phone(0, any1))
        .sets_up(thinks_needs_to_protect_self_from_intimacy(0)),

    MakeBeat("Goddess archetype says person important to the case had no " +
        "faith but you have to have faith.")
        .ok_if(
            wife_died_randomly(1),
            character_states.talking_to(1, 2),
            traits.is_goddess_archetype(2)
        )
        .sets_up(character_states.talking_to(1, nobody)),

    MakeBeat("Goddess archetype says you are living too much in where people " +
        "could be. Focus on where they are now.")
        .ok_if(
            isFormerCop(1),
            character_states.talking_to(1, 2),
            traits.is_goddess_archetype(2)
        )
        .sets_up(
            character_states.told_to_focus_on_where_people_are(1),
            character_states.talking_to(1, nobody)
        ),

    #TODO: if is_awkward(1) scene where someone is talking about a standoff with
    # police because a guy was accused of selling weapons out of shop, and 1
    # asks if that was true. There's an awkward silence and someone jokingly
    # asks if he's a cop and pats him on the head

    MakeBeat("Tries to buy drugs from a dude while his dad is there and then "
        + "he comes over and chews protag out.")
        .ok_if(character_states.told_to_go_smoke_weed(0))
        .sets_up(made_a_huge_faux_pas(0)),

    MakeBeat("PI slept and dreamed of heroin.")
        .ok_if(traits.is_pi(0), core.now_at(0, locations.pi_home))
        .sets_up(isFormerOpiumAdict(0)),

    MakeBeat("Has big conspiracy board with yarn and stuff")
        .if_not(character_states.has_guidance(0, any1))
        .ok_if(
            core.now_at(0, locations.pi_office),
            traits.is_protag(0),
            character_states.has_a_case(0)
        )
        .sets_up(traits.isObsessive(0)),

    MakeBeat("Sleeps with someone he just met. Sneaks out in the morning for " +
        "good reason related to case (expecting to catch someone at a certain" +
        " time or keeping a planned meeting). Later girl calls him and asks " +
        "if he knows how it amde her feel to wake up alone")
        .ok_if(
            inter_character_perceptions.are_attracted_to_each_other(1,2),
            character_states.has_appointment_tomorrow_morning(1)
        )
        .ok_if(
            inter_character_perceptions.are_attracted_to_each_other(1,2),
            character_states.wants_to_see_something_happen_tomorrow_morning(1)
        )
        .sets_up(traits.is_inconsiderate(1)),

    MakeBeat("Mom calls and talks for a long time while he just gives meeker"
        + " and shorter answers")
        .ok_if(traits.is_awkward(1), core.now_at(1, locations.pi_office))
        .if_not(
            core.now_at(1, locations.pi_home),
            traits.lives_with(1, any1),
            traits.is_mother_of(any1, 1)
        )
        .if_not(character_states.talking_on_phone(1, any1))
        .sets_up(
            wants_to_have_a_family_and_good_job_by_now(1),
            thinks_they_cant_be_happy_if_their_life_hasnt_progressed_as_they_expected(1),
            thinks_needs_to_protect_self_from_intimacy(1)
        ),

    MakeBeat("Writhes on ground from awkwardness.")
        .express(actions.writhe_on_ground, {"person": 0})
        .ok_if(
            core.now_at(0, locations.pi_home),
            traits.is_awkward(0),
            character_states.was_in_traumatic_awkward_situation(0)
        )
        .ok_if(
            core.now_at(0, locations.pi_home),
            traits.is_awkward(0),
            made_a_huge_faux_pas(0)
        )
        .if_not(writhed_on_the_ground(0))
        .sets_up(
            core.now_at(0, locations.pi_home),
            thinks_making_a_social_mistake_is_unforgivable(0),
            writhed_on_the_ground(0)
        ),

    MakeBeat("Appologizes to client for making incorrect accusation. Offers " +
        "to resign from case. Client accepts apology and says that she found "+
        "some boxes that came in on his ship in the garage. It was odd that " +
        "they were at the house so she looked through them and found " +
        "matroishka dolls stuffed with bags of white powder. So Client keeps "+
        "PI on because he does have good instincts.")
        .ok_if(
            character_states.made_incorrect_public_accusation(0),
            character_states.suggested_father_smuggled_drugs(0)
        )
        .sets_up(
            sincerely_applogized(0),
            learned_to_apologize_and_recover_from_mistakes(0)
        ),

    MakeBeat("Wife died suddenly. Her last words didn't mean anything.")
        .express(
            descriptions.picture_and_last_words, { "person": 1, "partner": 2 }
        )
        .if_not(wife_died_randomly(any1))
        .if_not(traits.is_awkward(1))
        .ok_if(core.is_character(2), core.now_at(1, locations.pi_office))
        .sets_up(wife_died_randomly(1)),

    MakeBeat("Wife last words become meaningful.")
        .ok_if(wife_died_randomly(1))
        .sets_up(regainFaith(1)),

    MakeBeat("PI and client become friends")
        .ok_if(learned_to_apologize_and_recover_from_mistakes(1))
        .sets_up(made_a_platonic_friend(1)),

    MakeBeat("Takes a risk and asks romantic interest to leave town with him")
        .ok_if(traits.is_gambler(1), traits.is_protag(1))
        .sets_up(run_off_together(1,2)),

    MakeBeat("Finally listed to beautiful lyricsa at karaoke")
        .ok_if(learned_to_see_how_the_cycle_life_and_death_shapes_the_world(1))
        .sets_up(finally_heard_the_lyrics_of_fleeting_love_in_karaoke_song(1)),

    MakeBeat("Spiraled into alchoholism")
        .ok_if(learned_that_there_are_no_absolutes(1))
        .sets_up(spiraled_into_alchoholism(1)),

    MakeBeat("Goes to live on a farm")
        .ok_if(traits.isObsessive(1))
        .sets_up(quit_being_pi_for_simple_life(1)),
]

logic = [
    #TODO: these are all phrased like it's after the hero has fulfilled it
    # but do I actually want to have stuff gated on that? Should we rewrite
    # these all to be phrased as that the hero needs something. Are we going to
    # going to gate stuff on having the need itself specifically established? 
    MakeLogic("The need is what the hero must do to get over their flaw.")
        .ok_if(learned_to_apologize_and_recover_from_mistakes(1))
        .ok_if(learned_to_enjoy_empathy(1))
        .ok_if(learned_love_is_worth_it_even_if_you_get_hurt(1))
        .ok_if(learned_to_see_how_the_cycle_life_and_death_shapes_the_world(1))
        .ok_if(learned_that_there_are_no_absolutes(1))
        .ok_if(became_content_with_meaninglessness_of_life(1))
        .ok_if(learned_to_not_miss_what_they_were_never_entitled_to(1))
        .ok_if(learned_how_people_act_in_modern_times(1))
        .ok_if(learned_to_be_content_following_own_principles(1))
        .ok_if(learned_to_stay_calm_in_social_situations(1))
        .sets_up(Hero.need),

    MakeLogic("The lie is why the hero cannot see their own flaw.")
        .ok_if(thinks_making_a_social_mistake_is_unforgivable(1))
        .ok_if(thinks_being_selfish_is_always_ok(1))
        .ok_if(thinks_needs_to_protect_self_from_intimacy(1))
        .ok_if(thinks_that_life_is_blissfully_unchainging(1))
        .ok_if(thinks_there_is_absolute_morality(1))
        .ok_if(thinks_needs_to_find_secret_purpose_to_start_living(1))
        .ok_if(
            thinks_they_cant_be_happy_if_their_life_hasnt_progressed_as_they_expected(1)
        )
        .ok_if(ties_self_esteem_to_acceptance_by_an_organization(1))
        .ok_if(thinks_they_need_to_lash_out_when_they_feel_uncomforable(1))
        .ok_if(thinks_making_others_uncomfortable_has_no_consequence(1))
        .sets_up(Hero.lie),

    MakeLogic("The lie turns the need into the want.")
        .ok_if(wants_to_be_in_proximity_of_someone_they_fancy(1))
        .ok_if(wants_to_have_hedonistic_fun_and_not_care_about_others(1))
        .ok_if(wants_to_work_hard_to_distract_from_personal_life(1))
        .ok_if(feels_cannot_relate_to_others_and_wants_to(1))
        .ok_if(wants_to_prove_pacificism_is_right(1))
        .ok_if(wants_to_find_deeper_meaning_in_life(1))
        .ok_if(wants_to_have_a_family_and_good_job_by_now(1))
        .ok_if(wants_to_prove_themself_as_loyal(1))
        .sets_up(Hero.want),

    MakeLogic("The lock-in is when the hero chooses to take the case, because" +
        " they think it will fullfill their want.")
        .ok_if(
            saw_has_no_wedding_ring_on(1, 2),
            inter_character_perceptions.is_attracted_to(1, 2)
        )
        .ok_if(thinks_this_case_can_prove_how_good_of_pi_they_are(1))
        .ok_if(heard_person_is_head_of_group_fighting_for_irv(1, 3))
        .ok_if(pis_boss_says_case_is_important(1))
        .sets_up(Hero.lock_in),

    MakeLogic("The lowest point is when the hero feels the worst and is given "+
        "no choice but to overcome their flaw to proceed.")
        .ok_if(made_a_huge_faux_pas(1))
        .ok_if(other_cop_died_because_of_info_protag_gave_mob_boss(1))
        .ok_if(pis_boss_undermines_the_investigation(1))
        .sets_up(Hero.lowest_point),

    MakeLogic("The sacrifice action is when the hero makes the choice that is "+
        "possible by overcoming their flaw and by doing so sacrifice part of " +
        "theirself.")
        .ok_if(sincerely_applogized(1))
        .ok_if(was_forced_to_empathize_with_someone_to_get_info(1))
        .ok_if(quit_smoking(1))
        .ok_if(killed_to_prevent_a_mob_war(1))
        .ok_if(
            didnt_hit_on_new_coworker_as_she_clearly_is_attracted_to_other_coworker(1)
        )
        .ok_if(quit_being_pi_for_simple_life(1))
        .ok_if(betrayed_and_killed_mob_boss(1))
        .ok_if(disobeyed_a_direct_order(1))
        .sets_up(Hero.sacrifice_action),

    MakeLogic("Is desperate for sex/romance.")
        .ok_if(character_states.acted_desperate_for_romance(0))
        .sets_up(wants_to_be_in_proximity_of_someone_they_fancy(0)),

    MakeLogic("Wants to work hard to distract from personal problems")
        .ok_if(
            thinks_needs_to_protect_self_from_intimacy(0),
            character_states.is_eager_to_take_case(0)
        )
        .sets_up(wants_to_work_hard_to_distract_from_personal_life(0)),

    MakeLogic("Made a faux pas.")
        #Made an incorrect accusation unnecessarily publicly and confidently
        .ok_if(character_states.made_incorrect_public_accusation(0))
        .sets_up(made_a_huge_faux_pas(0)),

    MakeLogic("If is a widow(er), was married at one point.")
        .ok_if(wife_died_randomly(1))
        .sets_up(traits.was_married_before(1)),

    MakeLogic("Knowingly making someone uncomfortable means you don't think "
        + "it's a big deal")
        .ok_if(character_states.knowingly_made_uncomfortable(1, 2))
        .sets_up(thinks_making_others_uncomfortable_has_no_consequence(1)),

    MakeLogic("Reacts violently when uncomfortable.")
        .ok_if(character_states.kicked_out_client(1, 2))
        .sets_up(thinks_they_need_to_lash_out_when_they_feel_uncomforable(1)),

    # TODO: if PI's ghost is a fear of placeA, final showdown should be at
    # placeA
]

anti_logic = [
    MakeAntiLogic("Can't introduce flaw too late in the story")
        .ok_if(
            traits.is_protag(1), structure.has_started(structure.act_2_scene_1)
        )
        .if_not(traits.is_awkward(1))
        .cant_set_up(traits.is_awkward(1)),

    MakeAntiLogic("Can't introduce flaw too late in the story")
        .ok_if(
            traits.is_protag(1), structure.has_started(structure.act_2_scene_1)
        )
        .if_not(traits.is_cocky(1))
        .cant_set_up(traits.is_cocky(1)),

    MakeAntiLogic("Can't call back someone who they were awkward to if they " +
        "haven't learned to recover from mistakes")
        .ok_if(character_states.was_awkward_to(2))
        .if_not(learned_to_apologize_and_recover_from_mistakes(1))
        .cant_set_up(character_states.started_phone_call_to(1, 2)),

    MakeAntiLogic("Cocky people need to learn the value of empathy to " +
        "understand why someone would do another a favor.")
        .ok_if(traits.is_cocky(1))
        .if_not(learned_to_enjoy_empathy(1))
        .cant_set_up(
            traits.can_understand_why_one_would_do_their_friend_a_favor(0)
        ),
]
