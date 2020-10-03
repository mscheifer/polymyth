from story import ContentPack, Object
from beats.core import is_character, is_location

from expression import humans
from expression import nouns
from . import accusations
from . import bar
from . import character_arcs
from . import client_home
from . import conversations
from . import fathers_apartment
from . import gangster
from . import home
from . import locations
from . import outings
from . import pet_shop
from . import phone_calls
from . import pi_office
from . import plots
from . import ramen_shop
from . import structure_beats
from . import thematic_beats
from . import traits

###############################################################################
# Mystery is just sleight of hand with descriptions. You tell the reader the
# answer but hide it in description or jokes or any writing for some other
# purpose.
###############################################################################
# When writing a new beat you might struggle to figure out where to put it. Is 
# this part of the plot so it should go in plot.py? Or is it for a character
# arc so it should go in character_arcs.py? Or is it a conversation start so it
# goes in conversations.py?
#
# Beats that establish multiple things have to be one beat. So if they establish
# something for the plot and something for a character arc, they have to be
# defined in one place. So it makes sense to have their own place separate from
# the plot and arc specific logic. Logic is easier than beats as we can always
# split a logic rule that establishes two concepts into two rules, so all plot
# and character arc logic can always be split across files. So it makes sense to
# have some organisation of beats that doesn't fit that. Some of the files here
# are organized by lociation but general conversation beats are in
# converations.py and there are some other files to group abstract kinds beats
# that can happen. There's no real rule here; the beats can be grouped into
# whatever sets seem to naturally match where we think similar beats would be
# when we want to add new ones.
# 
# These general beat files should try to establish as literal concepts as
# possible. Then the plots.py and character_arcs.py files are responsible for
# having rules to derive high level concepts from those literal ones.
###############################################################################
# When the PI gets information from someone, usually it's not that
# person just voluntarily saying something useful to the case. Usually the
# important information is some said offhandedly or the person complaining
# ("Yeah the bar burned down. Didn't see anybody do it. Coulda been an
# accident. Good riddence though. Now those trucks that smell like fish
# won't be coming by at all hours"). This makes the PI realize some goods
# from the docs were being shipped to the bar.
#
# Sometimes the PI can then skillfully get more information by pretending to
# be sympathizing. "Oh yeah those TESCO trucks I hate em too. They're all
# over town". "No these were Abraham's Fish with that big photo of a
# fisherman. If I ever saw that guy walking down the street I'd sock him
# without thinking twice."
#
# This example is in the ask_why_bar_burned_down action text.
###############################################################################
# We don't have any refusal-of-the-call scenes because they don't work that well
# in a mystery genre. Because I already know there is a mystery that will get
# solved, I don't believe that the detective will really refuse the case as if
# so there would be no story.
###############################################################################

alan =  Object("alan")
clementine =  Object("clementine")
david = Object("david")
julie = Object("julie")
sarah = Object("sarah")

objects = [
    alan,
    david,
    julie,
    sarah,

    outings.on_a_date,

    locations.bar,
    locations.client_home,
    locations.fathers_apartment,
    locations.pi_home,
    locations.pi_office,
    locations.ramen_shop,
    locations.the_streets,
    locations.unknown_location,
]

high_level_pre_established_concepts = [
    is_character(alan),
    is_character(clementine),
    is_character(david),
    is_character(julie),
    is_character(sarah),
]

pre_established_concepts = (
    high_level_pre_established_concepts +
    locations.pre_established_concepts
)

beats = (
    accusations.beats +
    bar.beats +
    character_arcs.beats +
    client_home.beats +
    conversations.beats +
    fathers_apartment.beats +
    gangster.beats +
    home.beats +
    pet_shop.beats +
    phone_calls.beats +
    plots.beats +
    ramen_shop.beats +
    structure_beats.beats +
    thematic_beats.beats
)

logic_rules = (
    accusations.logic +
    character_arcs.logic +
    plots.logic +
    structure_beats.logic
)

anti_logic_rules = (
    character_arcs.anti_logic +
    plots.anti_logic +
    structure_beats.anti_logic +
    traits.anti_logic
)

object_expressions = {
    alan: humans.man("Alan", "Marbury"),
    clementine: humans.woman("Clementine", "DeSoto"),
    david: humans.man("David", "Polk"),
    julie: humans.woman("Julie", "Hall"),
    sarah: humans.woman("Sarah", "Wilson"),
    locations.bar: nouns.bar,
    nobody: nouns.nobody,
    outings.on_a_date: nouns.on_a_date,
    locations.pi_home: nouns.home,
    locations.pi_office: nouns.office,
    locations.ramen_shop: nouns.ramen_shop,
    locations.the_streets: nouns.the_streets,
    locations.unknown_location: nouns.unknown_location,
}

content_pack = ContentPack(
    objects,
    pre_established_concepts,
    beats,
    logic_rules,
    anti_logic_rules,
    object_expressions
)
# A theory for cycles in the story:
#
# The situations the characters end up in are based on the theme / tone at that
# point. For exmaple if characters are far from home they can encounter a road
# that is broken and overgrown.
#
# Things happen to the characters based on the situations they are in. For
# example, one character may trip on the broken pavement.
#
# Characters can take action in response to things happening to them or their
# friends for example one character may go help their friend who tripped get
# back up.
#
# Actions move a character on their arc and change the theme / tone appropriate
# for that point in their arc. For example if characters have demonstrated that
# they care about each other / have each others back, they will encounter can
# encounter a high wall that they have to boost / pull each other up.
#
# If some kind of lost characters just climbed up a big wall, they can look
#  out and see where they are going and no longer feel lost.

# A theory for cycles in the story:
# 1. Conflict occurs
# 2. Address physical consequences
# 3. Confront internal consequences
# 4. Accept new reality

# TODO: if it feels like pacing is bad and story is losing steam. Consider using
# the scene_can_end concept to require all scenes to add a new wrinkle to the
# mystery / challenge an assuption / turn the case on it's head / etc.

#TODO: scene where character writes a letter that noone will ever read (they
#assume), or makes a recording noone will ever hear.

#TODO: if character is a gangster, daughter forms relationship with friend, then
# is forced to whack friend. Daughter can tell character did it or at least
# is on the same side as those who did. Never speaks to character again.

#TODO: perspective espoused by character: all human tragedy comes from
# the difference in size between the sexes. What actions does that lead this
# character to take?

# TODO: character arc for a side character: He spends his whole life taking care
# of a house and then realizes he doesn't have to. Decides to leave and try
# other kinds of work. Fits the theme of why we feel duty or obligation to stay
# where we are / keep doing what we've been doing. Like the sunken cost fallacy
# for life choices.
#  -  Another telling of a similar arc: a character wanted to do good things as
# a child, be true to oneself. Had to take a job to survive. Struggled to figure
# out what to do with life. Had a habit of falling into working hard and getting
# better at work because it's easier. Woke up one day and realized they were
# struggling so hard to do something didn't really care about.
#  -  The PIs need to look info what happened during an old legal case involving
# the missing father so they track down his attorney.
# "You used to work with X at the law firm. Everyone we talked to says you were
# the best laywer they had. You would have made partner if you had stayed on for
# another six months. Why did you leave?"
# "I kept asking myself, why are you here? I gave a shit for a while. I did. I
# worked hard cause I thought we were doing good work. That's why they all
# thought I was a good lawyer. But the partners didn't care. The old guys. They
# were a revolving door anyways. Hard to know your department head's vision when
# they change every 3 years. People were quitting and they didn't backfill. Case
# load piled up and we worked hard cause we cared and thought they would find
# someone as soon as they could. But they didn't. They didn't care. Clients
# dropped us cause they got lost in the shuffle. But it didn't matter. The firm
# was so big it can't die. SOme junior lawyer will join up and some client will
# sign on based on the name. Nobody remembers what they did five years ago. So
# why did I give so many years to them? I don't know. I couldn't remember. So I
# left."
#  -  "I just woke up one day and couldn't remember why I cared. Why I was
# working so hard. So I left."

# TODO: case of missing radio personality. They assume she was killed by
# an obsessive fan. At the end, turns out she ended show on purpose because she
# realized it hurt people by creating parasocial relationships.

# TODO: some options for the protagonist being a bad guy. Can have l'etranger
# ending where they find purpose in being hated. That's definitely a good option
# if player chooses to have protagonist just kille everyone. Can be like Millers
# Crossing or The Irishman where they have no connections to anyone in the end.
# Can do a cool "what heart" reveal moment that the protag is bad like in
# Miller's Crossing.

# TODO: word bank of mishearings to create mysteries based on that
