from story import Concept, MakeBeat, Object, any1, are_different

from beats import core
from expression import actions, modifiers
from . import character_states
from . import inter_character_perceptions
from . import locations
from . import outings
from . import self_perceptions
from . import traits
from .nobody import nobody

################################################################################
# Favor establishing traits and perceptions. Almost never gait on them unless
# the audience would be super surprised if the trait had not been established
# before. Audiences will accept new behaviors from characters as just more of
# their personality being discovered. When it wouldn't make sense for a
# character to say something, usually you will want to gate on not having a
# contradictory trait `if_not(contradictory_trait)` because probably it doesn't
# make sense as the character already said something before establishing
# something that doesn't gel with this behavior.
################################################################################

needsToHelpMom = Concept(1, "needsToHelpMom")
wasRejectedForDate = Concept(1, "wasRejectedForDate")
askOutAfterManyDates = Concept(1, "askOutAfterManyDates")
wantsToFightWaiter = Concept(1, "wantsToFightWaiter")

asked_if_father_left_town = Concept(0)
asked_if_i_talk_a_lot = Concept(2)
doesnt_take_client_seriously = Concept(0)
# TODO: this should have another parameter like a day so that it gets said again later
introductions_have_been_said = Concept(2)
# TODO: this should have another parameter like a day so that it gets said again later
pleasantries_have_been_said = Concept(2)

beats = [
    MakeBeat("Person is awkward, we learn from asking out on phone call")
        .ok_if(
            character_states.talking_on_phone(1, 2), are_different(2, nobody)
        )
        .if_not(traits.is_cocky(1))
        # because if he was in a loving marriage once he's not that awkward
        .if_not(traits.was_married_before(1))
        .express(actions.ask_what_are_you_up_to_this_weekend, {"person": 1})
        .express(actions.say_oh_not_much, {"person": 2})
        .express(
            actions.ask_if_want,
            {"asker": 1, "askee": 2, "thing": outings.on_a_date},
            modifiers.again,
            modifiers.specific_time
        )
        .sets_up(traits.is_awkward(1), needsToHelpMom(1)),

    MakeBeat("Person rejected")
        .ok_if(
            character_states.talking_on_phone(1, 2),
            are_different(2, nobody)
        )
        .express(actions.get_rejected, {"person": 1, "date": 2})
        .sets_up(
            traits.is_awkward(1),
            wasRejectedForDate(1),
            character_states.acted_desperate_for_romance(1),
            character_states.talking_on_phone(1, nobody)
        ),

    MakeBeat("Person wants to fight waiter")
        .ok_if(character_states.talking_on_phone(1,2))
        .if_not(traits.is_awkward(1))
        .express(actions.talk_about_fight_waiter, {"person": 1, "date": 2})
        .sets_up(traits.is_cocky(1), askOutAfterManyDates(1)),

    MakeBeat("Person is cocky on phone")
        .ok_if(
            traits.is_pi(1),
            character_states.talking_on_phone(1,2),
            wantsToFightWaiter(1)
        )
        .express(actions.be_cocky_on_phone, {"person": 1, "date": 2})
        .sets_up(
            traits.is_cocky(1),
            character_states.talking_to(1, nobody),
            character_states.talking_on_phone(1, nobody)
        ),

    MakeBeat("Someone meets PI in PI's office")
        .express(actions.meet_pi, {"pi": 0, "client": 1})
        .if_not(character_states.talking_to(0, any1))
        .if_not(inter_character_perceptions.have_met_before(0, 1))
        .ok_if(
            traits.is_pi(0),
            core.now_at(0, locations.pi_office),
            are_different(0, 1)
        )
        .sets_up(
            character_states.talking_to(0, 1),
            introductions_have_been_said(0, 1),
            core.now_at(1, locations.pi_office),
            traits.is_client(1),
            inter_character_perceptions.have_met_before(0, 1)
        ),

    MakeBeat("Say have met before and admire father")
        .ok_if(traits.is_pi(0), character_states.talking_to(0, 1))
        .express(
            actions.say_met_client_and_father_once_and_admire_father,
            {"pi": 0, "client": 1}
        )
        .sets_up(traits.is_father_of(2, 1), traits.know_each_other(0, 2)),

    MakeBeat("Ask after father")
        .express(
            actions.ask_after, {"person": 0, "conversation_partner_relative": 2}
        )
        .ok_if(
            character_states.talking_to(0, 1),
            introductions_have_been_said(0, 1)
        )
        .sets_up(
            traits.know_each_other(0, 2),
            traits.is_father_of(2, 1),
            character_states.asked_after_father(0, 1)
        ),

    MakeBeat("Tell someone father is missing")
        .express(actions.say_father_is_missing_for_3_days, {"client": 1})
        .ok_if(character_states.talking_to(1, 2))
        .sets_up(
            inter_character_perceptions.knows_father_of_1_is_missing(1, 2),
            character_states.missing_father_is_not_reason_for_being_here(1)
        ),

    MakeBeat("Ask if father left town")
        .ok_if(
            inter_character_perceptions.knows_father_of_1_is_missing(1, 0)
        )
        .express(actions.ask_if_father_left_town, {"pi": 0, "client": 1})
        .sets_up(asked_if_father_left_town, doesnt_take_client_seriously),

    #TODO:
    # if a character wants to be polite or nice to who they're talking to, ask
    # how they are doing.
    # If a character also knows the person's family ask after them as well.

    MakeBeat("Don't care what you think, eye roll.")
        .express(actions.state_dont_care_what_people_think, {"person": 0})
        .express(actions.roll_eyes, {"person": 1})
        .express(actions.look_hurt, {"person": 0})
        .ok_if(are_different(0, 1), character_states.talking_to(0, 1))
        .sets_up(traits.is_cocky(0), traits.is_insecure(0)),

    MakeBeat("Notices has no wedding ring on")
        .ok_if(core.now_at(1, 3), core.now_at(2, 3), are_different(1, 2))
        .sets_up(
            traits.is_awkward(1),
            inter_character_perceptions.saw_has_no_wedding_ring_on(1, 2),
            inter_character_perceptions.is_attracted_to(1, 2)
        ),

    MakeBeat("Says you talk a lot.")
        .express(actions.say_you_talk_a_lot, {"person": 1})
        .ok_if(character_states.talking_to(1, 2))
        .sets_up(
            traits.is_bold(1),
            self_perceptions.knows_they_might_talk_too_much(2),
            inter_character_perceptions.knows_talks_a_lot(1, 2)
        ),

    MakeBeat("Ask if I talk a lot.")
        .express(actions.ask_if_i_talk_a_lot, {"asker": 1, "askee": 2})
        .ok_if(
            character_states.talking_to(1, 2),
            # Confusing for the character to ask about this if it hasn't been
            # shown to the audience first.
            self_perceptions.knows_they_might_talk_too_much(1),
        )
        .sets_up(asked_if_i_talk_a_lot(1, 2), traits.are_friends(1, 2)),

    MakeBeat("Say yeah you do.")
        .express(actions.say_yeah_you_do, {"speaker": 1})
        .ok_if(asked_if_i_talk_a_lot(1, 2))
        .sets_up(
            self_perceptions.knows_for_sure_they_talk_too_much(2),
            traits.is_honest(1)
        ),

    MakeBeat("Lie and say no.")
        .express(actions.say_no_you_dont, {"speaker": 1})
        .ok_if(asked_if_i_talk_a_lot(1, 2))
        .sets_up(
            self_perceptions.knows_for_sure_they_talk_too_much(2),
            traits.can_lie(1)
        ),

    MakeBeat("Client saw PI in a dream")
        .ok_if(
            traits.is_pi(0),
            traits.is_client(1),
            core.now_at(0, 2),
            core.now_at(1, 2)
        )
        .express(actions.say_saw_pi_in_a_dream, {"pi": 0, "client": 1})
        .sets_up(inter_character_perceptions.trusts(1, 0)),

    MakeBeat("Bad guy alters the deal. Best bet it's not altered futher")
        .express(actions.say_altering_the_deal, {"person": 2})
        .ok_if(
            character_states.made_a_deal(1, 2),
            traits.is_asshole(2),
            traits.has_power_over(2, 1)
        )
        .sets_up(character_states.altered_the_deal(2, 1)),

    MakeBeat("Con artist charms anyone on to them and then pretends to pull " +
        "them into their inner circle")
        .express(actions.pretend_wasnt_trying_to_fool, {"con": 1, "fool": 2})
        .ok_if(
            traits.is_con_artist(1),
            character_states.accused_of_being_con_artist(2, 1)
        )
        .sets_up(character_states.is_charmed_by(2, 1)),
]
