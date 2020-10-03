from story import MakeBeat, any1, are_different

from beats import core
from expression import actions
from expression import descriptions
from . import cases
from . import locations
from . import traits

beats = [
    MakeBeat("Introduce Ramen shop owner")
        .express(descriptions.opened_shop_late_at_night, {"person": 1})
        .express(descriptions.served_late_night_customers, {"person": 1})
        .if_not(traits.is_protag(any1))
        .sets_up(
            traits.is_protag(1),
            traits.is_ramen_shop_owner(1),
            core.now_at(1, locations.ramen_shop)
        ),

    MakeBeat("Regular's father is missing")
        .express(actions.see_regular_walk_in, {"owner": 0, "regular": 1})
        .express(
            actions.hear_regular_father_is_missing, {"owner": 0, "regular": 1}
        )
        .ok_if(
            traits.is_ramen_shop_owner(0),
            core.now_at(0, locations.ramen_shop),
            core.is_character(1),
            are_different(0, 1)
        )
        .if_not(cases.case_of_missing_father(0))
        .sets_up(
            core.now_at(1, locations.ramen_shop),
            traits.is_regular(1),
            cases.case_of_missing_father(0)
        ),

    MakeBeat("Closes shop and leaves.")
        .express(actions.close_ramen_shop, {"owner": 0})
        .ok_if(
            traits.is_ramen_shop_owner(0), core.now_at(0, locations.ramen_shop)
        )
        .sets_up(core.now_at(0, locations.the_streets)),
]
