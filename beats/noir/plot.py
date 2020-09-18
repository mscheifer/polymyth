# NOTE: concepts from the HerosJourney should only be used in conditions (ok_if
# or if_not). In set_up, only the HerosJoruneyCharacterArc classes shoudl be
# used.
from beats.character_arcs import HerosJourney

hookScene = Object()
searchScene1 = Object()
searchScene2 = Object()
findScene1 = Object()
findScene2 = Object()
takeScene = Object()
returnScene = Object()

is_next_scene = Concept(2)

pre_established_concepts = [
    is_next_scene(hookScene, searchScene1)
    is_next_scene(searchScene1, searchScene2)
    is_next_scene(searchScene2, findScene1)
    is_next_scene(findScene1, findScene2)
    is_next_scene(findScene2, takeScene)
    is_next_scene(takeScene, returnSecene)
]

# hook: killer knew that he was diabetic and poisioned his insulin but he only
#   told close family because he didn't want to look weak (or something else
#   where the killer needs to know an intimate detail that the victim kept
#   secret from most people)
father_was_secret_diabetic_and_killed_with_poisoned_insulin = Concept(0)
# hunch: it seems like father's business partner killed him because he was going
#   to expose their shady dealings
fathers_business_partner_seems_like_he_did_it = Concept(0)
# twist: business parter was deliberately framed
fathers_business_partner_was_deliberately_framed = Concept(0)
# reveal: the client did it to inherit the money. Client is very clever to know
#   that the father was doing shady stuff with business partner so frame job
#   would seem convincing
the_client_killed_her_father_to_inherit_money = Concept(0)

# hook: Client says her BF's ex-wife is trying to get him committed to an insane
#   asylum. (The hook question is why the hell anyone would try to get someone
#   fradulently committed to an asylum, and how could they possibly succeed if
#   the person was not crazy?)
# hunch: Father seems to have gone missing and it seems like father's
#   disappearance is due to new hippy religious group that father had gotten
#   involved with
# twist: "insane asylum" is actually "rehab clinic". PI finds the name of the
#   one the father might be at
# reveal: Father is there voluntarily. He had his fun hanging out with the
#   hippy's but will be going back to his rich life afterward. "Go home little
#   man"

# hook: a mob boss hires PI, will double his fee but says it's a job he can't
#   refuse. PI needs to figure out which other mafia killed the mob boss's
#   lieutenant. (Hook question is: will PI survive this? (will he refuse and get
#   killed? will the other mafia figure out he's looking into them and kill
#   him?))
# hunch: It seems like the east side mafia was around when he was killed. They
#   have motive too as the lieutenant was trying to muscle into their teritory.
# twist: Members of the east side mafia approach the PI. PI thinks he will die
#   but mafia memebers say that the dead lieutenant was working for them. They
#   want to know who killed him too.
# reveal: Either the mob boss himself or someone else in their org did it
#   because he was working with the east side mafia. There's a mole for the mob
#   in the east side mafia who found out. Climax is east side mafia finds this
#   out and kills that guy. Mob retaliates and kills one of the east side guys.
#   Eventually everyone who knows that PI knew anything about this is dead so
#   he just walks away.

# hook: father is missing and scary threatening postcards are sent to the house
#   every day but they don't ask for money or anything (Hook question is why
#   would someone send these postcards with no clear motive but something must
#   be going on as father is missing).
# hunch: activists have been protesting at father's company. PI thinks one of
#   them may have kidnapped the father.
# twist: Turns out father ran away with his secretry to go free all the horses
#   in the state. Postcards are unrelated to that.
# reveal: PI finally looks into why people are protesting. Company was dumping
#   toxic waste into water supply (this was mentioned earlier in the story). PI
#   finds out protesters are threatening to blow up the company factory if they
#   don't stop. PI lets them in to go do it.

# hook: client claims father has amnesia and it's due to someone kidnapping him
#   and doing something unknown to him, as he was missing for 18 hours.
# hunch: Fathers company seems to be involved in shady real estate deals.
#   Someone unhappy with that may have attacked the father.
# twist: father had a psychotic break when he was reminded of a blocked memory
#   of killing his brother in a rage. The amnesia wasn't deliberate. His sister
#   who he hadn't seen since the incident found him after 35 years.
# reveal: TODO

# ================================================================
#
#
# hook - has 1 scene where audience is intrigued and wants to find out the
#     answer to the mystery. The hook is a question where the fact that there
#     can even be an answer is not obvious. Not just "who killed this person"
#     but like "who could have done something so evil as killed a baby and glued
#     it's eyes open to get kidnapping money" or "how could he have vanished
#     from this room when someone was watching the door the whole time". by the
#     end of the story the audience does know the answer and it makes perfect
#     sense based on the twist or reveal.
# search - has 2 scenes looking for clues at the end of which has a suspect
# find - has 2 scenes looking for clues to find suspect and the end of which
#     it is revealed suspect was a read herring and we know the real perp.
#     Revealing the real perp should also raise the stakes by either
#     recontextualizing the original crime or having there be an imminent
#     threat.
# take - has 1 scene where at the end the perp is caught
# return - has 1 scene where we see the aftermath. We confirm that everyone
#     found out the truth and stolen goods are returned (or we confirm the
#     opposite if the tone is nihilistic).
#

beats = [
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

    MakeBeat("Meet client have met before")
        .ok_if(
            isPI(0),
            talking_to(0, 1),
            is_father_of(2, 1)
        )
        .if_not(talking_on_phone(0, any1), are_different(any1, nobody))
        .express(actions.say_met_client_and_father_once_and_admire_father, {"pi": 0, "client": 1})
        .sets_up(know_each_other(0, 2)),

    MakeBeat("Father missing case")
        .ok_if(
            isPI(0),
            now_at(0, pi_office),
            isClient(1),
            now_at(1, pi_office),
            asked_after_father(0, 1)
        )
        .if_not(hasACase(0))
        .express(actions.hear_client_father_is_missing, {"pi": 0, "client": 1})
        .sets_up(caseOfMissingFather(0)),

    MakeBeat("Sister ran off case")
        .ok_if(
            isPI(0),
            now_at(0, pi_office),
            isClient(1),
            now_at(1, pi_office),
            asked_after_father(0, 1)
        )
        .if_not(hasACase(0))
        .express(actions.hear_daughter_has_run_off, {"pi": 0, "client": 1})
        .sets_up(hasACase(0)),

    MakeBeat("Ask if father left town")
        .ok_if(
            isPI(0),
            now_at(0, pi_office),
            isClient(1),
            now_at(1, pi_office),
            caseOfMissingFather(0)
        )
        .express(actions.ask_if_father_left_town, {"pi": 0, "client": 1})
        .sets_up(asked_if_father_left_town, doesnt_take_client_seriously),

    MakeBeat("Father being shady case")
        .ok_if(
            isPI(0),
            now_at(0, pi_office),
            isClient(1),
            now_at(1, pi_office),
            asked_after_father(0, 1)
        )
        .if_not(hasACase(0))
        .sets_up(hasACase(0)),

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

    MakeBeat("Takes gun out of desk")
        .express(actions.take_gun_out_of_desk, {"person": 0})
        .ok_if(now_at(0, pi_office), isProtag(0))
        #TODO: should use some special concepts to say anbody not the PI rather
        # than just checking against the client
        .if_not(now_at(any1, pi_office), isClient(any1))
        .sets_up(has_a_gun(0)),

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
        .express(descriptions.someone_robbed_protag, {})
        .ok_if(isProtag(0), now_at(0, pi_home))
        .sets_up(protagGotRobbed),

    MakeBeat("Finds match book from burglars")
        .express(actions.find_matchbook_from_burglars, {"protag": 0})
        .ok_if(protagGotRobbed, isProtag(0))
        .sets_up(burglarsHungOutAtBar()),

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
        .sets_up(talking_to(1, 2), is_old_boss(2), scene_cannot_end),

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
        .if_not(HerosJourneyPlot.search)
        .sets_up(now_at(0, bar)),

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
        .sets_up(
            joined_mysterious_woman_at_booth,
            talking_to(0, 1),
            is_goddess_archetype(1)
        ),

    MakeBeat("Talks to mysterious woman.")
        .ok_if(now_at(0, bar), joined_mysterious_woman_at_booth)
        .sets_up(talkedToMysteriousWoman),

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
        .sets_up(
            joined_mysterious_woman_at_booth,
            talking_to(0, 1),
            is_goddess_archetype(1)
        ),

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
        .sets_up(HerosJourneyPlot.search, talking_to(1, nobody)),

    MakeBeat("Mystery woman says you are not a real person. You're just " +
        "someone else's dream.")
        .ok_if(now_at(1, bar), talkedToMysteriousWoman)
        .if_not(HerosJourney.search)
        .sets_up(
            we_live_inside_a_dream,
            HerosJourneyPlot.search,
            talking_to(1, nobody)
        ),

    MakeBeat("Breaks into father's appartment.")
        .ok_if(isObsessive(1), caseOfMissingFather(1))
        .ok_if(hasGuidance(1,2), caseOfMissingFather(1))
        .sets_up(inFathersAppartment(1)),

    MakeBeat("Finds father dead.")
        .if_not(silly_tone)
        .ok_if(inFathersAppartment(1))
        .sets_up(serious_tone, foundDeadFather(1)),

    MakeBeat("Finds match book on father's body.")
        .ok_if(foundDeadFather(0))
        .sets_up(fatherHungOutAtBar()),

    MakeBeat("Finds paper with non-sensical phrases.")
        .ok_if(foundDeadFather(0))
        .sets_up(heardCodedWords),

    #TODO: PI is tailing someone. Follows them into a movie theater.
    # Movie that is playing is thematic
    # Thinks he sees the person sit down next to someone else. They look like
    # they're exchanging something, but it's hard to see.
    # Later in the story it turns out something else was happening.

    MakeBeat("Listens to nightclub singer. Realizes it's a coded message")
        .ok_if(now_at(0, bar), heardCodedWords)
        .sets_up(secretMessageSinger),

    MakeBeat("Leaves seedy bar.")
        .if_not(bar_burned_down)
        .ok_if(HerosJourney.search, now_at(0, bar))
        .sets_up(now_at(0, the_streets)),

    MakeBeat("Calls father's business. Asks questions. Finds out father's " +
        "secretary started a month long vacation 1 week before father " +
        "disappeared.")
        .if_not(was_awkward_to_fathers_secretary)
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
        "Asks bar neighbor why it burned down. Gets hint to go to docks."
    )
        .express(
            actions.ask_why_bar_burned_down,
            {"pi": 1, "bystander": 2},
            unnamed={"bystander": nouns.neighbor}
        )
        .express(descriptions.knows_fish_company_by_docks, {"pi": 1})
        .ok_if(isProtag(1), bar_burned_down, is_character(2), now_at(1, bar))
        .sets_up(HerosJourneyPlot.find, knows_to_check_out_docks(1)),

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
        .sets_up(foundEvidenceOfPerp(1,2), isPerp(2), HerosJourneyPlot.take),

    MakeBeat("Dog finds keys to free PI.")
        .ok_if(isChainedUp(0), isPI(0), dogCanFindKeys)
        .sets_up(isFree(0)),

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
        .sets_up(foundEvidenceOfPerp(1,1), isPerp(1), HerosJourneyPlot.take),

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
        .sets_up(protagGotShot, HerosJourneyPlot.theReturn),

    MakeBeat("Frog 1 is here and I'm going to get him..")
        .ok_if(chasing(1, 2), isObsessive(2))
        .sets_up(story_end),

    MakeBeat("Perp gets cornered down an alley.")
        .if_not(isObsessive(2))
        .ok_if(chasing(1,2))
        .sets_up(cornered(1,2)),

    MakeBeat("Perp pulls a gun. Fires on our hero and misses. PI kills perp.")
        .ok_if(cornered(1, 2), has_a_gun(2))
        .sets_up(died(1), HerosJourneyPlot.take, scene_can_end),

    MakeBeat("Protag throws gun away")
        .ok_if(protagGotShot, has_a_gun(1), isProtag(1))
        .sets_up(has_no_gun(1)),

    MakeBeat("Client learns who kidnapped/killed father and thanks PI for closure")
        .ok_if(isPerp(1), gotArrested(1))
        .ok_if(isPerp(1), died(1))
        .sets_up(HerosJourneyPlot.theReturn),

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
        .sets_up(HerosJourneyPlot.theReturn),

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
        .sets_up(HerosJourneyPlot.search),

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

    MakeBeat("Amnesiac goes to jewler to ask about ring they are wearing. " +
        "Amnesiac said they found the ring. Jewler says, 'this is not " +
        "something you find, this is something you kill for. I want no part " +
        "of this.")
        .ok_if(is_amnesiac(0))
        .sets_up(),
]

logic = [
    MakeRule("Start with a hook")
        .ok_if(father_was_secret_diabetic_and_killed_with_poisoned_insulin)
        # more...
        .sets_up(scene_can_end) #Or something to enable the hunch phase to begin

    MakeBeat("PI has followed his hunch")
        .ok_if(fathers_business_partner_seems_like_he_did_it)
        # more...
        .sets_up(scene_can_end) #Or something to enable the twist phase to begin

    MakeBeat("We have a twist")
        .ok_if(fathers_business_partner_was_deliberately_framed)
        # more...
        .sets_up(scene_can_end) #Or something to enable the reveal phase to begin

    MakeBeat("All is revealed")
        .ok_if(the_client_killed_her_father_to_inherit_money)
        # more...
        .sets_up(story_end)

    MakeBeat("Seems like father's business partner did it.")
        .ok_if(father_was_secret_diabetic_and_killed_with_poisoned_insulin)
        .ok_if(were_very_close(father, business_partner))
        .set_up(fathers_business_partner_seems_like_he_did_it)

    MakeBeat("Father's business partner was deliberately framed.")
        .ok_if(fathers_business_partner_seems_like_he_did_it)
        .ok_if(found_evidence_fathers_business_parter_was_framed)
        .set_up(fathers_business_partner_was_deliberately_framed)

    MakeBeat("The client killed her father's to inherit the money.")
        .ok_if(fathers_business_partner_was_deliberately_framed)
        .ok_if(found_evidence_client_framed_business_partner)
        .ok_if(killers_motive_was_to_inherit_money)
        .set_up(the_client_killed_her_father_to_inherit_money)

    # So this is good. We have some rules that something plot related needs to
    # happen so it doesn't feel like a pointless scene. Then we need other rules
    # to start scenes that check if the previous scene can end using the
    # is_previous_scene and can_end concepts, as well as specific prerequisites
    # like knowing something is up at the docks.
    #
    # Further refinemens we need are to lay out which types of scenes happen at
    # which point of heros journey and how many scenes there should be roughly.
    # And then build that as more concept logic.
    MakeRule("Got a case in this scene")
        .ok_if(pi_received_a_case_during('scene'))
        .sets_up(plot_progressed('scene')),

    MakeRule("Picked up a matchbook in this scene")
        .ok_if(picked_up_match_book_during('scene'))
        .sets_up(plot_progressed('scene')),

    MakeRule("Got a reason to check out the docks in this scene")
        .ok_if(learned_something_is_up_at_the_docks_during('scene'))
        .sets_up(plot_progressed('scene')),

    MakeRule("Plot progressed so can go to next scene")
        .ok_if(plot_progressed('scene'))
        .sets_up(can_end('scene')),
]
