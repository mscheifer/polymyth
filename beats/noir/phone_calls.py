from story import MakeBeat

from . import character_states
from . import traits

beats = [
    MakeBeat("Calls fathers secretary")
        .ok_if(traits.is_fathers_secretary(2))
        .sets_up(character_states.started_phone_call_to(1, 2)),

    MakeBeat("""Was able to call secretary up where their conversation earlier
        in the story was super awkward. PI apologizes and plays it off like
        they were super tired or upset that day and then the secretary accepts
        their apology and demonstration of not being so awkward and helps the
        PI out by saying that the father met with PI's mentor the day he
        disappeared.""")
        .ok_if(
            traits.is_fathers_secretary(2),
            character_states.started_phone_call_to(1, 2),
            character_states.has_guidance(1, 2)
        )
        .sets_up(character_states.knows_father_met_with(1, 2))
]
