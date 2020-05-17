# TODO: make this and the one in actions.py the same object defined somewher common
class Description:
    def __init__(self, *parameters):
        self.parameters = parameters

    def __repr__(self):
        return "Act(" + str(self.parameters) + ")"

# habitual behaviors
opened_shop_late_at_night = Description("person")
picture_and_last_words = Description("person", "partner")
served_late_night_customers = Description("person")
