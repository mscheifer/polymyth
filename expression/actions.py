class Action:
    def __init__(self, *parameters):
        self.parameters = parameters

    def __repr__(self):
        return "Act(" + str(self.parameters) + ")"

ask = Action("person")
ask_if_want = Action("asker", "askee", "thing")
ask_out_after_many_dates = Action("person")
ask_to_recount_forgotten_childhood = Action("person")
ask_what_are_you_up_to_this_weekend = Action("person")
be_cocky_on_phone = Action("person")
get_rejected = Action("person")
hear_client_father_is_missing = Action("person")
hear_regular_father_is_missing = Action("owner", "regular")
just_some_spring_cleaning = Action("person")
lean_back_in_chair = Action("person")
look_hurt = Action("person")
open_paper = Action("person")
read_political_scandal_in_paper = Action("person")
roll_eyes = Action("person")
say_i_stopped_caring_what_people_think = Action("person")
say_needs_to_help_mom = Action("person")
say_oh_not_much = Action("person")
see_client_walk_in = Action("person")
see_regular_walk_in = Action("owner", "regular")
see_shadows_of_people_following = Action("person")
state_dont_care_what_people_think = Action("person")
take_gun_out_of_desk = Action("person")
talk_about_fight_waiter = Action("person")
talk_show_ghosting = Action("person")
turn_on = Action("person", "thing")
twirl_phone_cord = Action("person")
walk_home_sees_shadows = Action("person")
walk_to = Action("person", "to")
watch_talk_show_about_ghosting = Action("person")
