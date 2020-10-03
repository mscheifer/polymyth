from story import (
    Concept,
    MakeAntiLogic,
    MakeBeat,
    MakeLogic,
    any1,
    are_different,
    story_end
)

from beats import core
from expression import actions
from expression import descriptions
from expression import modifiers
from . import animals
from . import cases
from . import character_states
from . import inter_character_perceptions
from . import locations
from . import plot
from . import themes
from . import traits
from . import world_state
from .nobody import nobody

# TODO Perp motives
# Love / sex
# Greed
# Revenge
# Madness

chasing = Concept(2, "chasing")
client_lied = Concept(0)

# 1st parameter is the perp, 2nd param is the detective
cornered = Concept(2, "cornered")

fathers_secretary_left_on_vacation = Concept(0)
feels_motivated = Concept(1)
found_evidence_client_framed_business_partner = Concept(0)
found_evidence_fathers_business_partner_was_framed = Concept(0)

# 1st parameter is the detective, 2nd param is the perp
foundEvidenceOfPerp = Concept(2, "foundEvidenceOfPerp")

is_framed = Concept(1)
is_in_satanic_cult = Concept(1)
killers_motive_was_to_inherit_money = Concept(0)
knows_father_went_to_bar = Concept(1)
must_call_for_alibi = Concept(2)
protagGotShot = Concept(0, "protagGotShot")
runsAway = Concept(1, "runsAway")
said_never_knew_father = Concept(1)
satanicCult = Concept(0, "satanicCult")
secretMessageSinger = Concept(0, "secretMessageSinger")
went_on_a_date_with = Concept(2)
wore_a_blue_rose = Concept(1)

############ DESCRIPTION OF PLOTS ##############################################
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
############ BEGIN PLOTS #######################################################

# hook: killer knew that he was diabetic and poisioned his insulin but he only
#   told close family because he didn't want to look weak (or something else
#   where the killer needs to know an intimate detail that the victim kept
#   secret from most people)
#   [[alt]] Victim was killed with gun in safe that only victim and daughter knew
#   the combination to.
father_was_killed_by_intimate_knowledge = Concept(0)
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
clients_boyfriends_ex_wife_is_trying_to_get_him_committed = Concept(0)
# hunch: Father seems to have gone missing and it seems like father's
#   disappearance is due to new hippy religious group that father had gotten
#   involved with
father_was_involved_with_new_religious_group = Concept(0)
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

# TODO: the reveal has to tie into the hook and hunch more. The perp has to be a
# character who matters somewhat in those stages.
# hook: Someone claiming to be a time traveler shows client a picture of them
#   dead. Says the dam that will be completed in 4 days will collapse
#   immediately. Then the figure flees.
# hunch: Investigating this mysterious figure, the PI finds their workshop where
#   they have stuff that looks like a time machine. Also there are more items
#   that seem to have traveled back from the past.
# twist: PI finds the time traveler who comes clean saying he faked it to try
#   and prevent what's about to happen. He knows the dam will fail. Why? because
#   he was one of the engineers.
# reveal: PI, fake time traveler, and client all talk. PI asks why traveler
#   didn't just tell client about the flaws. Traveler says client knows about
#   the flaws and just doesn't care. Client says she didn't know about them. All
#   the plans looked fine. Fake traveler says it would have been obvious. Turns
#   out that her construction manager was lying to her. He changed stuff to cut
#   costs and didn't listen to other engineers who said it would fail. When
#   client also vetoed the design he started sending her different plans than
#   what everyone else saw.

############ END PLOTS #########################################################

beats = [
    MakeBeat("Say sister ran off")
        .ok_if(
            traits.is_pi(0),
            core.now_at(0, locations.pi_office),
            traits.is_client(1),
            core.now_at(1, locations.pi_office)
        )
        .express(actions.hear_daughter_has_run_off, {"pi": 0, "client": 1})
        .sets_up(),

    MakeBeat("Father being shady case")
        .ok_if(
            traits.is_pi(0),
            core.now_at(0, locations.pi_office),
            traits.is_client(1),
            core.now_at(1, locations.pi_office),
            character_states.asked_after_father(0, 1)
        )
        .sets_up(cases.father_being_shady_case),

    MakeBeat(
        "Client gives PI a fake identity and has them eavesdrop on father at " +
        "fancy party."
    )
        .ok_if(
            traits.is_pi(1),
            cases.father_being_shady_case,
        )
        .if_not(character_states.knows_to_check_out_docks(1))
        .sets_up(character_states.knows_to_check_out_docks(1)),

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

    MakeBeat("#0 Walks home in the rain. Sees shadows of people following them.")
        .express(
            actions.walk_to,
            {"person": 0, "to": locations.pi_home},
            modifiers.in_rain
        )
        .express(actions.see_shadows_of_people_following, {"person": 0})
        .ok_if(traits.is_protag(0), core.now_at(0, locations.unknown_location))
        .sets_up(traits.isParanoid(0), core.now_at(0, locations.the_streets)),

    MakeBeat("Goes home.")
        .express(actions.go_home, { "person": 0})
        .express(descriptions.pi_at_home, { "pi": 0})
        .ok_if(traits.is_protag(0), core.now_at(0, locations.the_streets))
        .sets_up(core.now_at(0, locations.pi_home)),

    MakeBeat("Gets books. Hunkers down. Studies")
        # TODO: there needs to be some mystery in the case that the protag can
        # use scientific knowledge to work out. The beat should be gated on that
        # and then set up that the protag has figured out the case by the
        # knowledge making them suddenly realize something.
        .ok_if(
            traits.is_protag(0),
            feels_motivated(0),
            core.now_at(0, locations.pi_home),
            core.now_at(0, locations.pi_office)
        )
        .sets_up(),

    MakeBeat("Goes to missing father's office. Interviews secretary who is "
        "wearing a blue rose on her lapel.")
        .ok_if(cases.case_of_missing_father(0), traits.is_fathers_secretary(1))
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
        .ok_if(character_states.has_a_case(1), are_different(1, 2))
        .if_not(traits.is_client(2))
        .if_not(character_states.has_guidance(1, any1))
        .sets_up(character_states.talking_to(1, 2), traits.is_old_boss(2)),

    MakeBeat("Old boss suggests smoking weed to think about case with a "
        + "broadened perspective")
        .ok_if(character_states.talking_to(1, 2), traits.is_old_boss(2))
        .sets_up(character_states.told_to_go_smoke_weed(1)),

    MakeBeat("Finishes talking to old boss")
        .ok_if(character_states.talking_to(1, 2), traits.is_old_boss(2))
        .sets_up(
            character_states.has_guidance(1, 2),
            character_states.talking_to(1, nobody)
        ),

    MakeBeat("Finds paper with non-sensical phrases.")
        .ok_if(core.now_at('pi', locations.fathers_apartment))
        .ok_if(core.now_at('pi', locations.client_home))
        .sets_up(character_states.heard_coded_words('pi')),

    #TODO: PI is tailing someone. Follows them into a movie theater.
    # Movie that is playing is thematic
    # Thinks he sees the person sit down next to someone else. They look like
    # they're exchanging something, but it's hard to see.
    # Later in the story it turns out something else was happening.

    MakeBeat("Calls father's business. Asks questions. Finds out father's " +
        "secretary started a month long vacation 1 week before father " +
        "disappeared.")
        .if_not(
            character_states.was_awkward_to(any1),
            traits.is_fathers_secretary(any1)
        )
        .ok_if(
            character_states.told_to_focus_on_where_people_are('pi'),
            cases.case_of_missing_father('pi')
        )
        .sets_up(fathers_secretary_left_on_vacation),

    MakeBeat("Calls father's business. Tries to asks questions but is awkward.")
        .if_not(fathers_secretary_left_on_vacation)
        .ok_if(cases.case_of_missing_father(1), traits.is_awkward(1))
        .sets_up(
            character_states.was_awkward_to(2),
            traits.is_fathers_secretary(2)
        ),

    MakeBeat("Calls regular, says saw their father run into bar but lost him")
        .ok_if(
            core.now_at(0, locations.pi_home),
            character_states.told_to_focus_on_where_people_are(0),
            character_states.saw_missing_father_head_to_bar(0),
            traits.is_regular(1)
        )
        .sets_up(knows_father_went_to_bar(1)),

    # TODO: follow up with watching them perform a ritual that fails.
    # TODO: if supernatural established then maybe could be real
    MakeBeat("Finds out that dead father was in satanic cult.")
        # Require PI is obsessive for thematic reasons
        .ok_if(traits.isObsessive(1), cases.case_of_missing_father(1))
        .sets_up(character_states.found_motive(1), satanicCult),

    MakeBeat("Protag finds satanic cult hideout with blue rose as the symbol.")
        .ok_if(wore_a_blue_rose(0), satanicCult)
        .sets_up(is_in_satanic_cult(0)),

    MakeBeat("Overhears that dead father was involved in scandal.")
        .ok_if(world_state.political_scandal, cases.case_of_missing_father(1))
        .sets_up(character_states.found_motive(1)),

    MakeBeat("Finds evidence criminal mastermind did it.")
        .ok_if(
            character_states.found_motive(1),
            traits.isObsessive(1),
            are_different(1, 2)
        )
        .sets_up(foundEvidenceOfPerp(1,2), traits.is_perp(2)),

    MakeBeat("Dog finds keys to free PI.")
        .ok_if(
            character_states.isChainedUp(0),
            traits.is_pi(0),
            traits.can_find_keys(animals.dog)
        )
        .sets_up(character_states.isFree(0)),

    MakeBeat("""Old boss did it because victim was going to screw the town over
            by forging documents saying that he owned some desert land that was
            about to be irrigated, just like the victim had done once before
            long ago to say that a gold mine was on their land instead of public
            land.""")
        .ok_if(
            character_states.has_guidance(1,2),
            traits.is_perp(2),
            world_state.political_scandal
        )
        .sets_up(character_states.found_motive(1)),

    MakeBeat("""Old boss did it because he was a crooked PI who partnered with
            the victim and would steer the investiagation away from crooks who
            payed him off. Victim goes back to a cold case years later and won't
            drop it so old boss had to kill him.""")
        .ok_if(
            character_states.has_guidance(1,2),
            traits.is_perp(2),
            traits.is_pi(3),
            traits.is_victim(3)
        )
        .sets_up(character_states.found_motive(1)),

    MakeBeat("""Old boss did it because he was a mostly-straight PI but covered
            up for the crimes of his rich brother so that he would keep getting
            monetary gifts. The brother killed the victim accidentally,
            recklessly.""")
        .ok_if(character_states.has_guidance(1,2), traits.is_perp(2))
        .sets_up(character_states.found_motive(1)),

    MakeBeat("Turns out PI did it.")
        .ok_if(traits.is_violent(0), traits.is_psychopathic(0))
        .sets_up(foundEvidenceOfPerp(1,1), traits.is_perp(1)),

    MakeBeat("Goes to perps place.")
        .ok_if(foundEvidenceOfPerp(1,2))
        .sets_up(core.now_at(1, locations.perp_home)),

    MakeBeat("Perp sees PI and bolts.")
        .ok_if(core.now_at(0, locations.perp_home), traits.is_perp(1))
        .sets_up(runsAway(1)),

    MakeBeat("PI chases perp.")
        .ok_if(runsAway(1), core.now_at(2, locations.perp_home))
        .sets_up(chasing(1, 2)),

    MakeBeat("PI is shot in shoulder by perp while running")
        .ok_if(
            chasing(1, 2), character_states.has_a_gun(2), traits.is_protag(2)
        )
        .sets_up(protagGotShot),

    MakeBeat("Frog 1 is here and I'm going to get him..")
        .ok_if(chasing(1, 2), traits.isObsessive(2))
        .sets_up(story_end),

    MakeBeat("Perp gets cornered down an alley.")
        .if_not(traits.isObsessive(2))
        .ok_if(chasing(1,2))
        .sets_up(cornered(1,2)),

    MakeBeat("Perp pulls a gun. Fires on our hero and misses. PI kills perp.")
        .ok_if(cornered(1, 2), character_states.has_a_gun(2))
        .sets_up(character_states.died(1)),

    MakeBeat("Protag throws gun away")
        .ok_if(protagGotShot, character_states.has_a_gun(1), traits.is_protag(1))
        .sets_up(character_states.has_no_gun(1)),

    MakeBeat("Client learns who kidnapped/killed father and thanks PI for closure")
        .ok_if(traits.is_perp(1), character_states.got_arrested(1))
        .ok_if(traits.is_perp(1), character_states.died(1))
        .sets_up(),

    MakeBeat("Forget it Jake, it's Chinatown.")
        .ok_if(character_states.knows_perp_is_in_chinatown(1))
        .sets_up(story_end),

    MakeBeat("Tunrs out father ran off for silly reason.")
        # Reason could be to free all captive horses in the state or something
        # TODO: express that he ran off with a younger woman to do the silly
        # thing because he wanted some excitement in his life.
        .ok_if(themes.silly_tone, fathers_secretary_left_on_vacation)
        .sets_up(),

    MakeBeat("Instead of going to look for missing father, stays home and " +
        "reads a book. Later gets a call from client/regular saying they need" +
        "to drive out to Indio. The car ride is long and quiet")
        .ok_if(
            themes.we_live_inside_a_dream,
            cases.case_of_missing_father(0),
            traits.is_protag(0),
            traits.is_client(1)
        )
        .sets_up(
            core.now_at(0, locations.the_streets),
            core.now_at(1, locations.the_streets)
        ),

    MakeBeat("Realizes coded message was telling him to go check out the " +
        "waterfront.")
        .ok_if(secretMessageSinger, traits.is_protag(1))
        .sets_up(character_states.knows_to_check_out_docks(1)),

    MakeBeat("PI goes to the docks. Finds drug smuggling. Asks client about " +
        "it. Client initially plays if off but then admits she knew. PI asks " +
        "if she thinks that might be related to his disappearance. And why did"+
        " she not tell him. She says for obvious reasons she wants to keep it "+
        "on the DL. PI asks if she thought he wouldn't find out, angrily. He " +
        "is a PI after all.")
        .ok_if(character_states.knows_to_check_out_docks(1), traits.is_protag(1))
        .sets_up(client_lied),

    MakeBeat("Finds secret society warehouse on the pier.")
        .ok_if(character_states.knows_to_check_out_docks(1), traits.is_protag(1))
        .sets_up(),

    MakeBeat("Client's father was a member of a secret society. Society was "
        + "bringing in shipments of drug (not illegal, just unknown). PI "
        + "accidentally takes some. Runs off in delerium, seeing things.")
        .ok_if(
            traits.is_protag(0),
            cases.case_of_missing_father(0),
            character_states.knows_to_check_out_docks(0)
        )
        .sets_up(character_states.tripping(0)),

    MakeBeat("PI wakes up, his office is missing and nobody remembers him. He "
        + "takes the drug again and it all comes back")
        .ok_if(traits.is_pi(0), character_states.tripping(0))
        .sets_up(character_states.tripyExistentialCrisis(0)),

    MakeBeat("It was real. The PI learns that he is a small thing in a big "
        + "indifferent world he will never understand. He find's clients father"
        + "who says 'go home, little man'.")
        .ok_if(character_states.tripyExistentialCrisis(0))
        .sets_up(story_end),

    MakeBeat("Amnesiac goes to jewler to ask about ring they are wearing. " +
        "Amnesiac said they found the ring. Jewler says, 'this is not " +
        "something you find, this is something you kill for. I want no part " +
        "of this.")
        .ok_if(traits.is_amnesiac(0))
        .sets_up(),

    MakeBeat("Awkward protag is framed for murder so must call date who " +
        "rejected them to clear themself")
        #TODO: express call date on phone
        .express(actions.ask_how_are_you, {"person": 1})
        .express(
            actions.say_they_are_happy_just_being_alive_cooly, {"person": 2}
        )
        #TODO: express explain situation awkwardly 
        #TODO: express date helps 1 out
        .ok_if(went_on_a_date_with(1, 2), is_framed(1), traits.is_awkward(1))
        .sets_up(must_call_for_alibi(1, 2)),
]

logic = [
    MakeLogic("Start with a hook")
        .ok_if(father_was_killed_by_intimate_knowledge)
        .ok_if(clients_boyfriends_ex_wife_is_trying_to_get_him_committed)
        # more...
        .sets_up(plot.reader_is_hooked),

    # At the end of this scene, PI has found some evidence or heard some
    # interesting stuff to have a hunch for what might have happened and how
    # to go investigate that.
    MakeLogic("PI has a hunch")
        .ok_if(fathers_business_partner_seems_like_he_did_it)
        .ok_if(father_was_involved_with_new_religious_group)
        # more...
        .sets_up(plot.pi_has_a_hunch),

    MakeLogic("There is a twist")
        .ok_if(fathers_business_partner_was_deliberately_framed)
        # more...
        .sets_up(plot.we_had_a_twist),

    MakeLogic("All is revealed")
        .ok_if(the_client_killed_her_father_to_inherit_money)
        # more...
        .sets_up(plot.all_has_been_revealed),

    MakeLogic("Seems like father's business partner did it.")
        .ok_if(father_was_killed_by_intimate_knowledge)
        .ok_if(
            traits.were_very_close(1, 2),
            traits.is_father_of(1, 'c'),
            traits.is_client('c'),
            traits.is_fathers_business_partner(2),
        )
        .sets_up(fathers_business_partner_seems_like_he_did_it),

    MakeLogic("Father's business partner was deliberately framed.")
        .ok_if(fathers_business_partner_seems_like_he_did_it)
        .ok_if(found_evidence_fathers_business_partner_was_framed)
        .sets_up(fathers_business_partner_was_deliberately_framed),

    MakeLogic("The client killed her father's to inherit the money.")
        .ok_if(fathers_business_partner_was_deliberately_framed)
        .ok_if(found_evidence_client_framed_business_partner)
        .ok_if(killers_motive_was_to_inherit_money)
        .sets_up(the_client_killed_her_father_to_inherit_money),

    MakeLogic("The case of the missing father.")
        .ok_if(
            character_states.asked_after_father(0, 1),
            inter_character_perceptions.knows_father_of_1_is_missing(1, 0)
        )
        .sets_up(cases.case_of_missing_father(0)),

    MakeLogic("If they told PI their father is missing, PI could take the case.")
        .ok_if(
            traits.is_pi('pi'),
            inter_character_perceptions.knows_father_of_1_is_missing(1, 'pi')
        )
        .sets_up(traits.is_potential_client(1)),

    MakeLogic("Any case means has a case.")
        .ok_if(cases.case_of_missing_father(0))
        .ok_if(cases.father_being_shady_case, traits.is_pi(0))
        .sets_up(character_states.has_a_case(0)),

    MakeLogic("If PI's mentor lied about not knowing victim. They're the perp")
        .ok_if(
            said_never_knew_father('mentor'),
            character_states.knows_father_met_with('pi', 'mentor')
        )
        .sets_up(foundEvidenceOfPerp('pi', 'mentor'), traits.is_perp('mentor')),

    MakeLogic("Finally realizes money from victim to x was because they were " +
        "friends and victim was doing x a favor, which the PI couldn't " +
        "understand before because they assumed everyone is selfish. " +
        "Therefore x was lying about the money being for a business " +
        "arrangement and they did not personally know each other, so x is " +
        "very likely the perp or is in on it.")
        .ok_if(traits.can_understand_why_one_would_do_their_friend_a_favor(1))
        .sets_up(foundEvidenceOfPerp(1,2)),
]

anti_logic = [
    MakeAntiLogic("Can't have two perps") # To simplify for now
        .ok_if(traits.is_perp(any1), are_different(any1, 2))
        .cant_set_up(traits.is_perp(2))
]

# Lowest points
# TODO: PI's junior associate is killed
# TODO: PI is framed, cops are after him
# TODO: Finds father who doesn't want to be found ("go home little man")
# TODO: Thinks it was the client who did it. Confronts her and realizes he was
# wrong
# TODO: Fire at PI office or client house destroys all evidence they have found
# so far
# TODO: They kidnap someone's child that was shown in first act

#TODO:
# if early scene mentioned stamp collecting offhandedly
# then search for missing money turns out it was turned into rare stamps and
# hidden in plain sight
