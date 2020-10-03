from story import Concept, MakeBeat

from beats import core
from expression import actions
from expression import descriptions
from expression import nouns
from . import cases
from . import character_states
from . import locations
from . import themes
from . import traits
from .nobody import nobody

bar_burned_down = Concept(0)
joined_mysterious_woman_at_booth = Concept(0)
talkedToMysteriousWoman = Concept(0, "talkedToMysteriousWoman")

beats = [
    MakeBeat("Sees missing father on street and follows to seedy bar")
        .ok_if(
            traits.is_ramen_shop_owner(0), core.now_at(0, locations.the_streets)
        )
        .if_not(character_states.saw_missing_father_head_to_bar(0))
        .sets_up(
            core.now_at(0, locations.bar), character_states.saw_missing_father_head_to_bar(0)
        ),

    MakeBeat("Goes to seedy bar.")
        .express(
            actions.enters_seedy_bar,
            {"pi": 0, "doorman": 1},
            unnamed={"doorman": nouns.doorman}
        )
        .ok_if(
            character_states.knows_father_hung_out_at_bar(0),
            core.is_character(1)
        )
        .ok_if(
            character_states.knows_burglars_hung_out_at_bar(0),
            core.is_character(1)
        )
        .if_not(core.now_at(0, locations.bar))
        .sets_up(core.now_at(0, locations.bar)),

    # TODO: this could also be a fortune teller, so not at the bar
    MakeBeat("Asks about match book and meets mysterious woman")
        .ok_if(
            core.now_at(0, locations.bar),
            core.is_character(1),
            core.is_character(2),
            character_states.knows_father_hung_out_at_bar(0)
        )
        .ok_if(
            core.now_at(0, locations.bar),
            core.is_character(1),
            core.is_character(2),
            character_states.knows_burglars_hung_out_at_bar(0)
        )
        .express(
            actions.ask_about_match_book_then_meet_mysterious_woman,
            {"pi": 0, "bartender": 2, "ml": 1},
            unnamed={"bartender": nouns.bartender}
        )
        .express(actions.join_mysterious_woman, {"pi": 0})
        .sets_up(
            joined_mysterious_woman_at_booth,
            character_states.talking_to(0, 1),
            traits.is_goddess_archetype(1)
        ),

    MakeBeat("Talks to mysterious woman.")
        .ok_if(core.now_at(0, locations.bar), joined_mysterious_woman_at_booth)
        .sets_up(talkedToMysteriousWoman),

    MakeBeat("Follows father inside and meets mysterious woman")
        .ok_if(
            core.now_at(0, locations.bar),
            core.is_character(1),
            core.is_character(2),
            character_states.saw_missing_father_head_to_bar(0)
        )
        .if_not(joined_mysterious_woman_at_booth)
        .express(
            actions.follow_father_inside_then_meet_mysterious_woman,
            {"pi": 0, "bartender": 2, "ml": 1},
            unnamed={"bartender": nouns.bartender}
        )
        .express(actions.join_mysterious_woman, {"pi": 0})
        .sets_up(
            joined_mysterious_woman_at_booth,
            character_states.talking_to(0, 1),
            traits.is_goddess_archetype(1)
        ),

    # sets up for character change at the end, this is needed to accept
    # that the mentor was a bad guy
    MakeBeat("Mystery woman says client's father betrayed his own brother and "
        + "you have to accept loss.")
        .ok_if(
            core.now_at(1, locations.bar),
            traits.has_dead_brother(1),
            talkedToMysteriousWoman,
            cases.case_of_missing_father(1)
        )
        .sets_up(character_states.talking_to(1, nobody)),

    MakeBeat("Mystery woman says you are not a real person. You're just " +
        "someone else's dream.")
        .ok_if(core.now_at(1, locations.bar), talkedToMysteriousWoman)
        .sets_up(
            themes.we_live_inside_a_dream,
            character_states.talking_to(1, nobody)
        ),

    MakeBeat("Listens to nightclub singer. Realizes it's a coded message")
        .ok_if(
            core.now_at(0, locations.bar),
            character_states.heard_coded_words(0)
        )
        .sets_up(character_states.heard_secret_message_from_singer(0)),

    MakeBeat("Leaves seedy bar.")
        .if_not(bar_burned_down)
        .ok_if(core.now_at(0, locations.bar))
        .sets_up(core.now_at(0, locations.the_streets)),

    MakeBeat("Goes back to bar but it burned down")
        .if_not(core.now_at(1, locations.bar))
        .if_not(bar_burned_down)
        #TODO: somehow have a way to track if has visited locations before, and
        # gate on that instead of the two other reasons specifically
        .ok_if(
            character_states.knows_burglars_hung_out_at_bar(1),
            character_states.knows_father_hung_out_at_bar(1)
        )
        .ok_if(
            character_states.knows_burglars_hung_out_at_bar(1),
            character_states.saw_missing_father_head_to_bar(1)
        )
        .sets_up(bar_burned_down, core.now_at(1, locations.bar)),

    MakeBeat(
        "Asks bar neighbor why it burned down. Gets hint to go to docks."
    )
        .express(
            actions.ask_why_bar_burned_down,
            {"pi": 1, "bystander": 2},
            unnamed={"bystander": nouns.neighbor}
        )
        .express(descriptions.knows_fish_company_by_docks, {"pi": 1})
        .ok_if(
            traits.is_protag(1),
            bar_burned_down,
            core.is_character(2),
            core.now_at(1, locations.bar)
        )
        .sets_up(character_states.knows_to_check_out_docks(1)),
]
