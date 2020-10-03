from story import MakeBeat, MakeLogic

from beats import core
from . import character_states
from . import general_perceptions
from . import traits

beats = [
    MakeBeat("Makes accusation on flimsy evidence")
        .ok_if(
            traits.is_awkward(0),
            character_states.has_flimsy_evidence_against(0, 1),
            core.now_at(0, 'location'),
            core.now_at(1, 'location')
        )
        .ok_if(
            traits.is_cocky(0),
            character_states.has_flimsy_evidence_against(0, 1),
            core.now_at(0, 'location'),
            core.now_at(1, 'location')
        )
        .sets_up(character_states.accused(0, 1)),

    MakeBeat("Halucinate confession. Thinks it's real. Accuses the person " +
        "when waking up")
        .ok_if(
            traits.is_pi(0),
            character_states.is_injured_in_hospital(0),
            traits.is_cocky(0)
        )
        .sets_up(character_states.accused(0, 1)),
]

logic = [
    MakeLogic("Made an incorrect accusation unnecessarily publicly and " +
        "confidently.")
        .ok_if(
            character_states.accused(0, 1),
            general_perceptions.everyone_believes_is_not_perp(1)
        )
        .sets_up(character_states.made_incorrect_public_accusation(0)),
]
