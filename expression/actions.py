class Action:
    def __init__(self, *parameters):
        self.parameters = parameters

    def __repr__(self):
        return "Act(" + str(self.parameters) + ")"

# ml is mysterious lady

ask = Action("person")
ask_about_match_book_then_meet_mysterious_woman = Action(
    "pi", "bartender", "ml"
)
ask_if_want = Action("asker", "askee", "thing")
ask_if_father_left_town = Action("pi", "client")
ask_how_are_you = Action("person")
ask_out_after_many_dates = Action("person")
ask_to_recount_forgotten_childhood = Action("person")
ask_what_are_you_up_to_this_weekend = Action("person")
ask_who_could_have_killed_animals = Action("person")
ask_why_bar_burned_down = Action("pi", "bystander")
ask_why_you_didnt_know_where_from = Action("person1", "person2")
avoid_interaction_with_mother = Action("pi", "mother")
be_cocky_on_phone = Action("pi", "date")
close_ramen_shop = Action("owner")
enters_seedy_bar = Action("pi", "doorman")
encounter_sibyl = Action("client", "sibyl")
follow_father_inside_then_meet_mysterious_woman = Action("pi", "bartender", "ml")
find_wedding_ring_and_watch_on_counter = Action("pi")
get_rejected = Action("pi", "date")
go_home = Action("person")
hang_up = Action("person")
hear_client_father_is_missing = Action("pi", "client")
hear_daughter_has_run_off = Action("pi", "client")
hear_regular_father_is_missing = Action("owner", "regular")
join_mysterious_woman = Action("pi")
just_some_spring_cleaning = Action("person")
lean_back_in_chair = Action("person")
look_hurt = Action("person")
look_in_study = Action("pi", "client")
open_paper = Action("person")
read_political_scandal_in_paper = Action("person")
roll_eyes = Action("person")
say_distrust_moderate_drinkers = Action("person")
say_met_client_and_father_once_and_admire_father = Action("pi", "client")
say_needs_to_help_mom = Action("person")
say_oh_not_much = Action("person")
say_saw_pi_in_a_dream = Action("pi", "client")
say_they_are_happy_just_being_alive_cooly = Action("person")
#TODO: use this for a character who is emotionally abusive
say_you_can_talk_to_me_about_anything = Action("person")
#TODO: use this for a character who thinks they can demand their partner's time
# in a replationship
say_you_have_to_drink = Action("person")
see_client_walk_in = Action("pi", "client")
see_regular_walk_in = Action("owner", "regular")
see_shadows_of_people_following = Action("person")
state_dont_care_what_people_think = Action("person")
take_gun_out_of_desk = Action("person")
talk_about_fight_waiter = Action("pi", "date")
talk_show_ghosting = Action("person")
talk_to_client_father_while_both_trapped = Action("pi", "client_father")
talk_to_depressed_person = Action("depressed_person", "other_person")
talk_to_murderer = Action("murderer", "victim")
talk_to_seductress_on_phone = Action("person", "seductress")
turn_on = Action("person", "thing")
twirl_phone_cord = Action("person")
walk_home_sees_shadows = Action("person")
walk_to = Action("person", "to")
want_to_give_up = Action("client")
watch_talk_show_about_ghosting = Action("person")
writhe_on_ground = Action("person")
