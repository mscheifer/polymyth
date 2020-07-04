from story import Concept, Object

is_location = Concept(1, "isLocation")
is_character = Concept(1, "isCharacter")

now_at_location = Concept(
    1, "nowAtLocation", num_value_parameters=1
)
def now_at(character, location):
    return now_at_location.current([character], [location])

_scene_can_end_obj = Object("scene_can_end_obj")
_scene_cannot_end_obj = Object("scene_cannot_end_obj")

_scene_can_possibly_end = Concept(
    0, "sceneCanEnd", num_value_parameters=1
)

# The intention with these concepts is that the engine might start a scene for
# whatever reason and it would be weird if we just ended the scene immediately
# after or if the scene ended half way through so this is just some simple state
# logic that can be used contextually to make sure that something substantial
# always happens in a scene.
scene_can_end = _scene_can_possibly_end.current([], [_scene_can_end_obj])
scene_cannot_end = _scene_can_possibly_end.current([], [_scene_cannot_end_obj])

#TODO: might be a good idea to explicitly track arc resolutions when each
# character is introduced, and then gate the story ending on those all having
# happened. Dunno how to implement it exactly though.
