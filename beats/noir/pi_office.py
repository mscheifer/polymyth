from story import Concept, MakeBeat, any1, any2, are_different

from beats import core
from expression import actions
from . import character_states
from . import inter_character_perceptions
from . import locations
from . import structure
from . import traits
from . import world_state
from .nobody import nobody

would_not_want_to_come_back_to = Concept(2)

beats = [
    MakeBeat("Introduce PI in office")
        .if_not(traits.is_protag(any1))
        #TODO: should these structure checks be anti-logic in plots.py?
        .if_not(structure.is_done(structure.act_1_scene_1))
        .ok_if(
            core.is_character(1), structure.has_started(structure.act_1_scene_1)
        )
        .express(actions.lean_back_in_chair, {"person": 1})
        .sets_up(
            traits.is_protag(1),
            traits.is_pi(1),
            core.now_at(1, locations.pi_office)
        ),

    MakeBeat("Reads political scandal in paper")
        .express(actions.open_paper, {"person": 0})
        .express(actions.read_political_scandal_in_paper, {"person": 0})
        .if_not(core.now_at(any1, locations.pi_office), traits.is_client(any1))
        .if_not(character_states.talking_on_phone(0, any2))
        .ok_if(core.now_at(0, locations.pi_office), traits.is_protag(0))
        .sets_up(world_state.political_scandal),

    MakeBeat("Takes gun out of desk")
        .express(actions.take_gun_out_of_desk, {"person": 0})
        .ok_if(core.now_at(0, locations.pi_office), traits.is_pi(0))
        .if_not(core.now_at(any1, locations.pi_office), are_different(any1, 0))
        .sets_up(character_states.has_a_gun(0)),

    MakeBeat("Someone enters PI office")
        .express(actions.invite_in_to_office, {"pi": 0})
        .if_not(core.now_at(any1, locations.pi_office)) # for any other char
        .if_not(would_not_want_to_come_back_to(1, 0))
        .if_not(character_states.talking_to(0, any2))
        .ok_if(
            traits.is_pi(0),
            core.now_at(0, locations.pi_office),
            are_different(0, 1)
        )
        .sets_up(core.now_at(1, locations.pi_office)),

    MakeBeat("PI is on the phone")
        .ok_if(
            traits.is_pi(1),
            core.now_at(1, locations.pi_office),
            core.is_character(2)
        )
        .if_not(core.now_at(any1, locations.pi_office), traits.is_client(any1))
        .if_not(
            character_states.talking_on_phone(1, any1),
            are_different(any1, nobody)
        )
        .express(actions.twirl_phone_cord, {"person": 1})
        .sets_up(
            character_states.talking_on_phone(1, 2),
            character_states.talking_to(1, 2)
        ),

    MakeBeat("Someone enters PI office while PI is on the phone.")
        .if_not(core.now_at(any1, locations.pi_office)) # for any other char
        .if_not(would_not_want_to_come_back_to(1, 0))
        .ok_if(
            traits.is_pi(0),
            core.is_character(1),
            core.now_at(0, locations.pi_office),
            character_states.talking_on_phone(0, 2),
            are_different(0, 1)
        )
        .sets_up(core.now_at(1, locations.pi_office)),

    MakeBeat("Hang up because see someone entered")
        .express(actions.hang_up, {"person": 0})
        .ok_if(
            core.now_at(1, locations.pi_office),
            core.now_at(0, locations.pi_office),
            traits.is_pi(0),
            character_states.talking_on_phone(0, 2)
        )
        .sets_up(character_states.talking_on_phone(0, nobody)),

    MakeBeat("Say 'here because father in trouble'. He is missing.")
        .ok_if(
            traits.is_pi(0),
            core.now_at(0, locations.pi_office),
            traits.is_client(1),
            core.now_at(1, locations.pi_office),
            character_states.asked_after_father(0, 1)
        )
        .if_not(character_states.missing_father_is_not_reason_for_being_here(1))
        # Client uses this phrasing as a reference to her intent in stopping by
        # the PI's office. "just the thing" meaning just the reason she is here.
        .express(
            actions.hear_client_father_is_in_trouble, {"pi": 0, "client": 1}
        )
        .express(actions.say_father_is_missing_for_3_days, {"client": 1})
        .sets_up(inter_character_perceptions.knows_father_of_1_is_missing(1, 0)),

    MakeBeat("Is very eager to take case")
        .ok_if(
            core.now_at(0, locations.pi_office),
            traits.is_potential_client(1),
            core.now_at(1, locations.pi_office)
        )
        .sets_up(
            character_states.is_eager_to_take_case(0), traits.is_client(1)
        ),

    MakeBeat("PI tells client they love them. Client goes home. PI leaves")
        .ok_if(
            traits.is_pi(0),
            traits.is_client(1),
            core.now_at(0, locations.pi_office),
            core.now_at(1, locations.pi_office)
        )
        .if_not(character_states.talking_on_phone(0, any1))
        .sets_up(
            traits.is_creepy(0),
            character_states.knows_is_creepy(1, 0),
            core.now_at(0, locations.unknown_location),
            core.now_at(1, locations.unknown_location),
            character_states.knowingly_made_uncomfortable(0, 1)
        ),

    MakeBeat("Yells at client to get out. Leaves.")
        .ok_if(
            traits.is_pi(0),
            traits.is_client(1),
            core.now_at(0, locations.pi_office),
            core.now_at(1, locations.pi_office)
        )
        .if_not(character_states.talking_on_phone(0, any1))
        .sets_up(
            character_states.kicked_out_client(0, 1),
            core.now_at(0, locations.unknown_location),
            core.now_at(1, locations.unknown_location)
        ),

    MakeBeat("Second client comes in, sounds like they're also involved in " +
        "the case. Then when the secretary goes home the fake client pulls a " +
        "gun.")
        # TODO gate on 'go' because this shouldn't happen in act 1
        .ok_if(
            traits.is_pi(1),
            core.now_at(1, locations.pi_office),
            core.is_character(2),
            are_different(1, 2)
        )
        .if_not(traits.is_client(2))
        .sets_up(character_states.has_a_gun(2)),
]

logic = [
    MakeBeat("If the PI was a dick to someone they won't go seeking their help "
        + "again")
        .if_not(character_states.knows_is_creepy('c', 'p'))
        .if_not(character_states.kicked_out_client('p', 'c'))
        .sets_up(would_not_want_to_come_back_to('c', 'p'))
]
