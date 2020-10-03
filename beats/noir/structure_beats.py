from story import MakeAntiLogic, MakeLogic, MakeBeat

from expression import actions
from . import character_arcs
from . import plot
from . import required_payoffs
from . import structure

beats = [
    MakeBeat("Act 1 scene 1 start")
        .express(actions.scene_transition, {})
        .sets_up(structure.has_started(structure.act_1_scene_1)),

    MakeBeat("Act 1 scene 2 start")
        .express(actions.scene_transition, {})
        .ok_if(structure.is_done(structure.act_1_scene_1))
        .sets_up(structure.has_started(structure.act_1_scene_2)),

    MakeBeat("Act 2 scene 1 start")
        .express(actions.scene_transition, {})
        .ok_if(structure.is_done(structure.act_1_scene_2))
        .sets_up(structure.has_started(structure.act_2_scene_1)),

    MakeBeat("Act 2 scene 2 start")
        .express(actions.scene_transition, {})
        .ok_if(structure.is_done(structure.act_2_scene_1))
        .sets_up(structure.has_started(structure.act_2_scene_2)),

    MakeBeat("Act 3 scene 1 start")
        .express(actions.scene_transition, {})
        .ok_if(structure.is_done(structure.act_2_scene_2))
        .sets_up(structure.has_started(structure.act_3_scene_1)),

    MakeBeat("Act 3 scene 2 start")
        .express(actions.scene_transition, {})
        .ok_if(structure.is_done(structure.act_3_scene_1))
        .sets_up(structure.has_started(structure.act_3_scene_2)),
]

logic = [
    MakeLogic("Act 1 scene 1 done")
        .ok_if(plot.reader_is_hooked)
        .sets_up(structure.is_done(structure.act_1_scene_1)),

    MakeLogic("Act 1 scene 2 done")
        .ok_if(
            character_arcs.Hero.need,
            character_arcs.Hero.lie,
            character_arcs.Hero.want,
            character_arcs.Hero.lock_in
        )
        .sets_up(structure.is_done(structure.act_1_scene_2)),

    MakeLogic("Act 2 scene 1 done")
        .ok_if(plot.pi_has_a_hunch)
        .sets_up(structure.is_done(structure.act_2_scene_1)),

    MakeLogic("Act 2 scene 2 done")
        .ok_if(plot.we_had_a_twist, character_arcs.Hero.lowest_point)
        .sets_up(structure.is_done(structure.act_2_scene_2)),

    MakeLogic("Act 3 scene 1 done")
        .ok_if(character_arcs.Hero.sacrifice_action)
        .sets_up(structure.is_done(structure.act_3_scene_1)),

    MakeLogic("Act 3 scene 2 done")
        .ok_if(
            plot.all_has_been_revealed,
            character_arcs.Hero.boon,
        )
        .sets_up(structure.is_done(structure.act_3_scene_2)),
]

anti_logic = [
    MakeAntiLogic("")
        .ok_if(required_payoffs.needs_payoff(1))
        .if_not(required_payoffs.payed_off(1))
        .cant_set_up(structure.is_done(structure.act_3_scene_2)),
]
