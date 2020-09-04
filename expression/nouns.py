import ids

class ProperNoun:
    def __init__(self, raw_name, raw_last_name=None):
        self.raw_name = raw_name
        self.raw_last_name = raw_last_name
    def __repr__(self):
        name = self.raw_name
        if self.raw_last_name is not None:
            name += " " + self.raw_last_name
        return "PN(" + name + ")"

bar = ids.get_id()
bartender = ids.get_id()
doorman = ids.get_id()
home = ids.get_id()
neighbor = ids.get_id()
nobody = ids.get_id()
office = ids.get_id()
on_a_date = ids.get_id()
patrolman = ids.get_id()
ramen_shop = ids.get_id()
television = ids.get_id()
the_streets = ids.get_id()
unknown_location = ids.get_id()
