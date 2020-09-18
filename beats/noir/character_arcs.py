from story import Concept
# NOTE: concepts from the HerosJourney should only be used in conditions (ok_if
# or if_not). In set_up, only the HerosJoruneyCharacterArc classes shoudl be
# used.
from beats.character_arcs import HerosJourney

# Backstories (a.k.a The Ghost):
# A good backstory is when characters blame themselves for something bad, as
# they must have character growth to overcome it.
isFormerCop = Concept(1, "isFormerCop")
isFormerOpiumAdict = Concept(1, "isFormerOpiumAdict")
hasDeadBrother = Concept(1, "deadBro")
wifeDiedRandomly = Concept(1, "wifeDiedRandomly")

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

class HerosJourneyCharacterArc:
    go = Concept(0)
    change = Concept(0)

#TODO: character change: learns that desires to kiss girlfriend on beach
# aren't about any real person, just ideas from movies

#TODO: Character arc for awkward pi:
# -  he talks about how his grandfather built a house when he was 25. Ends
#    up not being a very good PI and client does most of the work to solve
#    case. protag quits being a PI and becomes a carpenter or construction
#    worker.

beats = [
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

    MakeBeat("Goddess archetype says person important to the case had no " +
        "faith but you have to have faith.")
        .ok_if(wifeDiedRandomly(1), talking_to(1, 2), is_goddess_archetype(2))
        .if_not(HerosJourney.search)
        .sets_up(HerosJourneyCharacterArc.search, talking_to(1, nobody)),

    MakeBeat("Goddess archetype says you are living too much in where people " +
        "could be. Focus on where they are now.")
        .ok_if(isFormerCop(1), talking_to(1, 2), is_goddess_archetype(2))
        .if_not(HerosJourney.search)
        .sets_up(
            told_to_focus_on_where_people_are,
            HerosJourneyCharacterArc.search,
            talking_to(1, nobody)
        ),

    #TODO: if isAwkward(1) scene where someone is talking about a standoff with
    # police because a guy was accused of selling weapons out of shop, and 1
    # asks if that was true. There's an awkward silence and someone jokingly
    # asks if he's a cop and pats him on the head

    MakeBeat("Tries to buy drugs from a dude while his dad is there and then "
        + "he comes over and chews protag out.")
        .ok_if(told_to_go_smoke_weed, isProtag(0))
        .sets_up(made_a_huge_faux_pas(0)),

    MakeBeat("PI slept and dreamed of heroin.")
        .if_not(ProtagonistDefinition.ghost)
        .ok_if(isPI(0), now_at(0, pi_home))
        .sets_up(isFormerOpiumAdict(0), ProtagonistDefinition.ghost),

    MakeBeat("Has big conspiracy board with yarn and stuff")
        .if_not(hasGuidance(0, any1))
        .ok_if(now_at(0, pi_office), isProtag(0), hasACase(0), HerosJourney.go)
        .sets_up(isObsessive(0)),

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

    MakeBeat("Wife died suddenly. Her last words didn't mean anything.")
        .express(descriptions.picture_and_last_words, { "person": 1, "partner": 2 })
        .if_not(wifeDiedRandomly(any1))
        .if_not(ProtagonistDefinition.ghost)
        .if_not(isAwkward(1))
        .ok_if(is_character(2), now_at(1, pi_office))
        .sets_up(wifeDiedRandomly(1), ProtagonistDefinition.ghost),

    MakeBeat("Wife last words become meaningful.")
        .ok_if(wifeDiedRandomly(1), HerosJourney.theReturn)
        .sets_up(regainFaith(1), HerosJourneyCharacterArc.change),

    MakeBeat("PI and client become friends")
        .ok_if(
            learned_to_apologize_and_recover_from_mistakes(1),
            HerosJourney.theReturn
        )
        .sets_up(made_a_platonic_friend(1), HerosJourneyCharacterArc.change),

    MakeBeat("Takes a risk and asks romantic interest to leave town with him")
        .ok_if(is_gambler(1), isProtag(1))
        .sets_up(run_off_together(1,2)),

    MakeBeat("Finally listed to beautiful lyricsa at karaoke")
        .ok_if(
            learned_to_see_how_the_cycle_life_and_death_shapes_the_world(1),
            HerosJourney.theReturn
        )
        .sets_up(
            finally_heard_the_lyrics_of_fleeting_love_in_karaoke_song(1),
            HerosJourneyCharacterArc.change
        ),

    MakeBeat("Spiraled into alchoholism")
        .ok_if(
            learned_that_there_are_no_absolutes(1),
            HerosJourney.theReturn
        )
        .sets_up(spiraled_into_alchoholism(1), HerosJourneyCharacterArc.change),

    MakeBeat("Goes to live on a farm")
        .ok_if(isObsessive(1), HerosJourney.theReturn)
        .sets_up(
            quit_being_pi_for_simple_life(1),
            HerosJourneyCharacterArc.change
        ),
]

logic = [
    MakeLogic("The lock-in moment is needed to cross the threshold.")
        .ok_if(saw_has_no_wedding_ring_on)
        .ok_if(thinks_this_case_can_prove_how_good_of_pi_they_are)
        .ok_if(heard_person_is_head_of_group_fighting_for_irv)
        .ok_if(pis_boss_says_case_is_important)
        .sets_up(HerosJourneyCharacterArc.go),
]
