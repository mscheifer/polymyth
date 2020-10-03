from story import Concept, MakeBeat, any1, are_different

from beats import core
from expression import actions
from expression import descriptions
from expression import nouns
from . import animals
from . import character_states
from . import locations
from . import themes
from . import traits

got_robbed = Concept(1, "piGotRobbed")

beats = [
    MakeBeat("Watches talk show. Guest jokes about ghosting.")
        .ok_if(traits.is_pi(0), core.now_at(0, locations.pi_home))
        .express(actions.turn_on, {"person": 0, "thing": nouns.television})
        .express(actions.watch_talk_show_about_ghosting, {"person": 0})
        .sets_up(),

    MakeBeat("Avoids talking to mom.")
        .ok_if(
            traits.is_pi(0),
            core.now_at(0, locations.pi_home),
            core.is_character(1),
            are_different(0, 1)
        )
        .if_not(traits.is_mother_of(any1, 0), are_different(1, any1))
        .express(
            actions.avoid_interaction_with_mother, {"person": 0, "mother": 1}
        )
        .sets_up(
            traits.is_awkward(0),
            traits.lives_with(0, 1),
            traits.is_mother_of(1, 0)
        ),

    MakeBeat("Wakes up disheveled. Asks dog to find keys while getting dressed.")
        .ok_if(core.now_at(0, locations.pi_home), traits.is_creepy(0))
        .ok_if(core.now_at(0, locations.pi_home), traits.isObsessive(0))
        .sets_up(character_states.asked_dog_to_find_keys(0)),

    MakeBeat("Has to find keys because dog obviously can't.")
        .ok_if(character_states.asked_dog_to_find_keys(1))
        .if_not(character_states.found_keys(1))
        .sets_up(character_states.found_keys(1)),

    MakeBeat("Dog can actually find keys.")
        .if_not(themes.serious_tone)
        .if_not(character_states.found_keys(0))
        .ok_if(
            character_states.asked_dog_to_find_keys(0),
            core.now_at(0, locations.pi_home),
            traits.is_pi(0)
        )
        .sets_up(
            traits.can_find_keys(animals.dog),
            character_states.found_keys(0),
            themes.silly_tone
        ),

    MakeBeat("Someone robbed Protag")
        .express(descriptions.someone_robbed_protag, {})
        .ok_if(core.now_at(0, locations.pi_home))
        .sets_up(got_robbed(0)),

    MakeBeat("Finds match book from burglars")
        .express(actions.find_matchbook_from_burglars, {"protag": 0})
        .ok_if(got_robbed(0))
        .sets_up(character_states.knows_burglars_hung_out_at_bar(0)),
]
