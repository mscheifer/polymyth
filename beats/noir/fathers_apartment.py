from story import Concept, MakeBeat

from beats import core
from . import cases
from . import character_states
from . import locations
from . import themes
from . import traits

foundDeadFather = Concept(1, "foundDeadFather")

beats = [
    MakeBeat("Breaks into father's appartment.")
        .ok_if(traits.isObsessive(1), cases.case_of_missing_father(1))
        .ok_if(
            character_states.has_guidance(1,2), cases.case_of_missing_father(1)
        )
        .sets_up(core.now_at(1, locations.fathers_apartment)),

    MakeBeat("Finds father dead.")
        .if_not(themes.silly_tone)
        .ok_if(core.now_at(1, locations.fathers_apartment))
        .sets_up(themes.serious_tone, foundDeadFather(1)),

    MakeBeat("Finds match book on father's body.")
        .ok_if(foundDeadFather(0))
        .sets_up(character_states.knows_father_hung_out_at_bar(0)),
]
