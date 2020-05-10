from story import Concept

is_location = Concept(1, "isLocation")
is_character = Concept(1, "isCharacter")

now_at_location = Concept(
    1, "nowAtLocation", num_value_parameters=1
)
def now_at(character, location):
    return now_at_location.current([character], [location])
