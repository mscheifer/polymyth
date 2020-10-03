from story import Concept, MakeBeat

from . import traits

stole_car = Concept(1)

beats = [
    MakeBeat("1 breaks into car. Takes out a big ring of keys and tries each " +
        "one by one. Looking calmly straight ahead the whole time.")
        .ok_if(traits.is_gangster(1))
        .sets_up(stole_car(1)),
]
