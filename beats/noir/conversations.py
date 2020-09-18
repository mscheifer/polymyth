have_met_before = Concept(2)
knows_father_of_1_is_missing = Concept(2)

# TODO: this should have another parameter like a day so that it gets said again later
introductionss_have_been_said = Concept(2)
# TODO: this should have another parameter like a day so that it gets said again later
pleasantries_have_been_said = Concept(2)

beats = [
    MakeBeat("Client meets PI")
        .express(actions.meet_pi, {"pi": 0, "client": 1})
        .if_not(talking_to(0, any1))
        .if_not(have_met_before(0, 1))
        .ok_if(
            isPI(0),
            now_at(0, pi_office),
            are_different(0, 1)
        )
        .sets_up(
            talking_to(0, 1),
            introductions_have_been_said(0, 1),
            now_at(1, pi_office),
            isClient(1),
            have_met_before(0, 1)
        ),

    MakeBeat("Ask after father")
        .express(
            actions.ask_after, {"person": 0, "conversation_partner_relative": 2}
        )
        .ok_if(
            talking_to(0, 1),
            introductions_have_been_said(0, 1),
            know_each_other(0, 2),
            is_father_of(2, 1)
        }
        .sets_up(asked_after_father(0, 1)),

    MakeBeat("Tell someone father is missing")
        .express(actions.say_father_is_missing_for_3_days, {"client": 1})
        .ok_if(talking_to(1, 2))
        .ok_if(caseOfMissingFather('pi'))
        .sets_up(knows_father_of_1_is_missing(1, 2)),

    MakeBeat("Tell someone father is missing")
        .express(actions.say_father_is_missing_for_3_days, {"client": 1})
        .ok_if(talking_to(1, 2))
        .if_not(hasACase('pi'))
        .sets_up(knows_father_of_1_is_missing(1, 2), caseOfMissingFather('pi')),

    #TODO:
    # if a character wants to be polite or nice to who they're talking to, ask
    # how they are doing.
    # If a character also knows the person's family ask after them as well.
]
