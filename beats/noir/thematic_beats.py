from story import Concept, MakeBeat, any1

from beats import core
from . import character_states
from . import themes
from . import traits

is_clients_father_brother = Concept(1)

beats = [
    MakeBeat("""If PI has a dead brother, establish that PI and brother shared
            everything and helped each other out when they were poor. Just
            before he died they had an argument where brother accused PI of
            drifting away because he had made some money and new friends. PI
            always regretted not saying the right thing in that moment.""")
        .ok_if(traits.has_dead_brother(0), traits.is_pi(0))
        .sets_up(themes.theme_of_money_conflict_between_siblings),

    MakeBeat("""Client's father has an older estranged brother who PI goes and
            speaks to even though client says not to. Father's older brother
            tells PI stories about client's father that give PI leads to
            investigate stuff.""")
        .if_not(is_clients_father_brother(any1))
        .ok_if(core.is_character(1))
        .sets_up(
            is_clients_father_brother(1),
            themes.theme_of_money_conflict_between_siblings
        ),

    MakeBeat("""At the end turns out client's father's older brother who is poor
            killed the father because he never shared his wealth and older
            brother thought he was owed it for raising client's father (as their
            parents had died""")
        .ok_if(is_clients_father_brother(1))
        .sets_up(character_states.found_motive(2), traits.is_perp(1)),

    # TODO: if antagonist has pretended to be someone else, final showdown in
    # house of mirrors
]
