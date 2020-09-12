# TODO: make this and the one in actions.py the same object defined somewher common
class Description:
    def __init__(self, *parameters):
        self.parameters = parameters

    def __repr__(self):
        return "Act(" + str(self.parameters) + ")"

# habitual behaviors
opened_shop_late_at_night = Description("person")
served_late_night_customers = Description("person")

knows_fish_company_by_docks = Description("pi")
pet_shop_massacre = Description("pi")
picture_and_last_words = Description("person", "partner")
pi_at_home = Description("pi")
someone_robbed_protag = Description()
