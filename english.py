#TODO Probably the plan that makes the most sense is just to keep writing and 
# wait until I actually want to re-use some prose to start abstracting.

import prose

# The philosophy here is that the experience will be like Groundhog Day. The
# beat choices will always give the same output, so it's ok if the same text
# appears in the same place in the story every time, or if similar text appears
# there for minor variations. We do want to avoid the same text appearing again
# later in the story though.

text = {
    prose.walks_home_sees_shadows: ("%0:n: walked home in the rain. %0:sp: saw "
    + "shadows of people following %0:op:."),
    prose.introduce_pi:
    "%1:n: leaned back in %1:pp: chair and propped %1:pp: legs up on %1:pp: desk.",
    prose.pi_on_phone:
    "%1:pp: fingers twirled the phone cord.",
    prose.what_are_you_up_to_this_weekend: 
    "What are you up to this weekend?",
    prose.just_some_spring_cleaning: 
    "Oh not much. Just some spring cleaning. You?",
    prose.needs_to_help_mom: 
    ("I gotta stop by my mom's place at some point to help her move a " +
    "bookcase. But that's about it."),
    prose.ask_out_dinner: 
    "Say, how would you like to get dinner again Saturday night?",
    prose.pi_rejected:
    """"Oh, your going to go help your mom out? That's so nice... Well... I
    don't think I want to see you again. You seemed very quiet and uncomfortable
    around me."
    "Wait now, that was just the first date. I was trying to be respectful. I
    can be more... I wasn't uncomfortable."
    "Anyway, I've got to go. Have a nice weekend."
    Jake put the receiver down and sat up.""",
    prose.pi_phone_ask_out_after_many_dates: 
    ("That's what I'm saying. You and me, out on the town again. That sax " +
    "player you like is playing again at Charlie's."),
    prose.pi_phone_fight_waiter: 
    """"Are you going to pick a fight with the waiter again? I'm surprised you
    think they'll let you back in the place."
    "I think he and I came to an understanding. Even if not, wouldn't you want
    to watch me give him a good one, huh? Right in the kisser."
    "Wow, you've well fixed on this guy. Maybe I should give you space to get to
    know him." """,
    prose.pi_phone_cocky: 
    """"You're real funny, girl. Why don't I come pick you up at 7:00"
    "How about this. Don't call me again until you've found some decency."
    "Wait what? Sarah?... Hello?"
    Jake put the receiver down and twirled his thumbs.""",

    #TODO: character arc for awkward version is that he has to make a difficult
    # decision at climax and be confident
    #TODO: Character arc for cocky version is?

    prose.client_walks_in:
    """He had been drumming his fingers and staring at the wall when he heard a nock on the door.
    "Come on in"
    "Good evening Mr Marbury. May I have a seat?"
    "Please, Ms." He struck out his hand.""",
    prose.pi_met_client_and_father_once_and_pi_admire_father:
    """"Goodhall, but we have been aquainted before. You came to my Father's
    60th birthday party 4 years back."
    "Ahh... yes of course. Your father was a great man from all the stories I
    had heard and I was glad to meet him. How is he?" """,
    prose.father_missing_case:
    """ "That's just the thing," she took a cigarette holder from her purse and
    withdrew one. Lighting it with a match. "He may be in trouble."
    "What kind of trouble"
    "I don't know. He hasn't been seen in 3 days." """,
    prose.pi_doesnt_take_confident_client_seriously:
    """"Did he go out of town? Take a little vacation."
    "He would never without telling someone." """,
    prose.father_not_at_san_diego_house_awkward_pi:
    """"Does he own a summer beach house. Somewhere he likes to get away."
    "Yes. A place in San Diego. I went there two days ago. He is not there. And
    again, if he went he would have told me." """,
    prose.pi_takes_the_case:
    """"Ok, ok. Where did you last see him?"
    "At the house for breakfast on Thursday."
    "I guess we can start there." """,
    prose.awkward_pi_confident_client_fees_and_go_to_client_house:
    """She rose from the chair. "Thank you for helping. I drove my car over here. Follow me?"
    "Yes certainly," Jake said getting up. "By the way my fee structure is fourty doll..."
    "Fourty dollars a day plus expenses. I read your sign on the door." She turned and left.
    Jake followed.""",

    prose.i_stopped_caring_what_people_think:
    "Maybe that would have shook me before I was 10 and stopped caring what people think",

    prose.rolled_their_eyes:
    "%0:n: rolled their eyes.",

    prose.looked_hurt:
    "%0:n: frowned and looked away.",

    prose.father_was_dishonest:
    """"My name is Jake Marbery. I believe you used to work with my father Sam Marbury."
    "Oh yes, I remember him. He did _______ work for a couple years a few decades back."
    "Yeah he had a _______ business back then."
    "That's true. He may have lied about other things but that was true." """,

    prose.takes_gun_out_of_desk:
    ("%0:n: opened a drawer in %0:pp: desk. %0:sp: withdrew a gun and holstered "
    + "it under his jacket."),

    prose.opened_shop_late_at_night:
    "%1:n: opened the shop every day at 10 pm and closed it again at 8 am.",
    prose.served_late_night_customers:
    "%1:sp: served taxi drivers, bar tenders and graveyard shift workers.",
}

"""

Jake and the client walked down a long dusty road.
"You know. I came to you because I knew you from a dream."
Jake looked at her.
"I dreamed I was riding a horse through the darkest night. I was so tired. I saw
a fire in the distance and rode for it. It was your camp. You shared some beans
with me..."
"I was eating a can of beans?" Jake laughedA
The client laughed too. "It's silly imaging a city boy eating beans straight
from a can. But you don't worry about things like that in a dream."

"""

#TODO use
""""Hundreds of letters from your father lie unopened but a single note from
your sister and you upend your life and your business?" """

#TODO: rewrite
"""The house lights dimmed. The band started a low jazz number. Spotlights from the
back of the room began spinning. The lights came together, drawing every eye in
the crowd to to the curtain, which parted revealing a woman in a blue sequin
dress. The spotlights moved again, casting layered shadows across her face. It
looked like she was changing into a different person."""
#TODO: she starts singing coded message

#TODO (if awkward PI):
# How are you?
# I'm alive, which is pretty engaging
