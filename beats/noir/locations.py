from story import Object

from beats import core

bar = Object("bar")
client_home = Object("client_home")
fathers_apartment = Object("fathers_apartment")
perp_home = Object("perp_home")
pet_shop = Object("pet_shop")
pi_home = Object("pi_home")
pi_office = Object("pi_office")
ramen_shop = Object("ramen_shop")
the_streets = Object("the_streets")
unknown_location = Object("unknown_location")

pre_established_concepts = [
    core.is_location(bar),
    core.is_location(client_home),
    core.is_location(fathers_apartment),
    core.is_location(pi_home),
    core.is_location(pi_office),
    core.is_location(ramen_shop),
    core.is_location(the_streets),
    core.is_location(unknown_location),
]
