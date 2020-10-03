from story import Concept, MakeBeat, Object

from beats import core
from expression import actions
from . import cases
from . import character_states
from . import inter_character_perceptions
from . import locations
from . import required_payoffs
from . import traits

client_is_hiding_something = Object()

thinks_father_wanted_to_leave_family = Concept(0)

beats = [
    MakeBeat("Look in study")
        .ok_if(
            traits.is_pi(0),
            core.now_at(0, locations.client_home),
            traits.is_client(1),
            core.now_at(1, locations.client_home)
        )
        .express(actions.look_in_study, {"pi": 0, "client": 1})
        .sets_up(
            required_payoffs.needs_payoff(client_is_hiding_something),
            inter_character_perceptions.is_suspicious_of(0, 1)
        ),

    MakeBeat("PI asks about south american maps on the wall. Client says her " +
        "father liked to sail down to South America frequently. PI suggests he"+
        " may have been drug smuggling. Client says he would never. PI asks to"+
        " check out father's boat and client says to drop it.")
        .ok_if(
            traits.is_pi(0),
            core.now_at(0, locations.client_home),
            traits.is_client(1),
            core.now_at(1, locations.client_home),
            cases.case_of_missing_father(0)
        )
        .sets_up(
            character_states.suggested_father_smuggled_drugs(0),
            inter_character_perceptions.is_suspicious_of(0, 1)
        ),

    # This seems like he wanted to leave his family but really he just wanted
    # to do the dishes.
    MakeBeat("Finds wedding ring and watch on counter")
        .ok_if(
            traits.is_pi(0),
            core.now_at(0, locations.client_home),
            cases.case_of_missing_father(0)
        )
        .express(actions.find_wedding_ring_and_watch_on_counter, {"pi": 0})
        .sets_up(thinks_father_wanted_to_leave_family),
]
