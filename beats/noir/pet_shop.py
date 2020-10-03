from story import MakeBeat, any1

from beats import core
from expression import actions
from expression import descriptions
from expression import nouns
from . import locations
from . import structure
from . import traits

beats = [
    MakeBeat("Introduce PI at crime scene")
        .express(descriptions.pet_shop_massacre, {"pi":1})
        .express(
            actions.ask_who_could_have_killed_animals,
            {'person': 2},
            unnamed={"person": nouns.patrolman}
        )
        .if_not(traits.is_protag(any1))
        .if_not(structure.is_done(structure.act_1_scene_1))
        .ok_if(
            core.is_character(1),
            core.is_character(2),
            structure.has_started(structure.act_1_scene_1)
        )
        .sets_up(
            traits.is_protag(1),
            traits.is_pi(1),
            core.now_at(1, locations.pet_shop)
        ),

    MakeBeat("Finds match book at crime scene")
        .express(actions.find_matchbook_at_crime_scene, {"pi": 1})
        .ok_if(core.now_at(1, locations.pet_shop))
        .sets_up(),
]
