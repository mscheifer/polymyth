import random

import expression.actions as actions
import expression.descriptions as descriptions
import expression.modifiers as modifiers
import expression.nouns as nouns
import prose

# The philosophy here is that the experience will be like Groundhog Day. The
# beat choices will always give the same output, so it's ok if the same text
# appears in the same place in the story every time, or if similar text appears
# there for minor variations. We do want to avoid the same text appearing again
# later in the story though.

todo_use_these = [
    #pi_met_client_and_father_once_and_pi_admire_father:
    """"Goodhall, but we have been aquainted before. You came to my Father's
    60th birthday party 4 years back."
    "Ahh... yes of course. Your father was a great man from all the stories I
    had heard and I was glad to meet him. How is he?" """,
    #pi_doesnt_take_confident_client_seriously:
    """"Did he go out of town? Take a little vacation."
    "He would never without telling someone." """,
    #father_not_at_san_diego_house_awkward_pi:
    """"Does he own a summer beach house. Somewhere he likes to get away."
    "Yes. A place in San Diego. I went there two days ago. He is not there. And
    again, if he went he would have told me." """,
    #pi_takes_the_case:
    """"Ok, ok. Where did you last see him?"
    "At the house for breakfast on Thursday."
    "I guess we can start there." """,
    #awkward_pi_confident_client_fees_and_go_to_client_house:
    """She rose from the chair. "Thank you for helping. I drove my car over here. Follow me?"
    "Yes certainly," Jake said getting up. "By the way my fee structure is fourty doll..."
    "Fourty dollars a day plus expenses. I read your sign on the door." She turned and left.
    Jake followed.""",

    #father_was_dishonest:
    """"My name is Jake Marbery. I believe you used to work with my father Sam Marbury."
    "Oh yes, I remember him. He did _______ work for a couple years a few decades back."
    "Yeah he had a _______ business back then."
    "That's true. He may have lied about other things but that was true." """,
]

actions_text = {
    actions.ask_if_want: [
        "Do you like to",
        "Do you want to",
        "How about we",
        "How would you like to",
        "Would you like to",
        "Would you want to",
    ],
    actions.ask_to_recount_forgotten_childhood: ("Wait, tell me about our " +
        "old friends, after school, running in the park. We thought we saw " +
        "something magical in the woods. I have forgotten now, but you " +
        "might still remember"),
    actions.ask_out_after_many_dates: 
        ("That's what I'm saying. You and me, out on the town again. That sax " +
        "player you like is playing again at Charlie's."),
    actions.ask_what_are_you_up_to_this_weekend: 
        "What are you up to this weekend?",
    actions.be_cocky_on_phone: 
        """"You're real funny, girl. Why don't I come pick you up at 7:00"
        "How about this. Don't call me again until you've found some decency."
        "Wait what? Sarah?... Hello?"
        Jake put the receiver down and twirled his thumbs.""",
    actions.get_rejected:
        """"Oh, your going to go help your mom out? That's so nice... Well... I
        don't think I want to see you again. You seemed very quiet and uncomfortable
        around me."
        "Wait now, that was just the first date. I was trying to be respectful. I
        can be more... I wasn't uncomfortable."
        "Anyway, I've got to go. Have a nice weekend."
        Jake put the receiver down and sat up.""",
    actions.hear_client_father_is_missing:
        """ "That's just the thing," she took a cigarette holder from her purse and
        withdrew one. Lighting it with a match. "He may be in trouble."
        "What kind of trouble"
        "I don't know. He hasn't been seen in 3 days." """,
    actions.lean_back_in_chair:
        "leaned back in %1:pp: chair and propped %1:pp: legs up on the desk",
    actions.look_hurt: "frowned and looked away",
    actions.open_paper: "cracked open the afternoon Chronicle",
    actions.read_political_scandal_in_paper:
        "In big bold letters it read: SENATOR WYDEN'S CORRUPT LAND DEAL",
    actions.roll_eyes: "rolled their eyes",
    actions.say_needs_to_help_mom: ("I gotta stop by my mom's place at some " +
        "point to help her move a bookcase. But that's about it."),
    actions.say_oh_not_much:
        "Oh not much. Just some spring cleaning. You?",
    actions.see_client_walk_in:
        """He had been drumming his fingers and staring at the wall when he
        heard a knock on the door.
        "Come on in"
        "Good evening Mr Marbury. May I have a seat?"
        "Please, Ms." He struck out his hand.""",
    actions.see_shadows_of_people_following:
        "saw shadows of people following %op",
    actions.state_dont_care_what_people_think: ("Maybe that would have shook " +
        "me before I was 10 and stopped caring what people think"),
    actions.take_gun_out_of_desk: ("opened a drawer in %0:pp: desk. %0:sp: " +
        "withdrew a gun and holstered it under his jacket."),
    actions.talk_about_fight_waiter: 
        """"Are you going to pick a fight with the waiter again? I'm surprised you
        think they'll let you back in the place."
        "I think he and I came to an understanding. Even if not, wouldn't you want
        to watch me give him a good one, huh? Right in the kisser."
        "Wow, you've well fixed on this guy. Maybe I should give you space to get to
        know him." """,
    actions.turn_on: "turned on the",
    actions.twirl_phone_cord: "fingers twirled the phone cord",
    actions.walk_to: "walked",
    actions.watch_talk_show_about_ghosting: ("The host was in the middle of " +
        "asking his guest. 'Have you ever ghosted anyone?' 'Well I ghosted my" +
        " guitar teacher.' Canned laughter."),
}

descriptions_text = {
    descriptions.opened_shop_late_at_night:
        "opened the shop every day at 10 pm and closed it again at 8 am.",
    descriptions.served_late_night_customers:
        "served taxi drivers, bar tenders and graveyard shift workers.",
}

nouns_text = {
    nouns.home: "home",
    nouns.on_a_date: [
        "out to dinner",
        "on a date",
    ],
    nouns.television: "television set",
}

modifiers_text = {
    modifiers.again: "again",
    modifiers.in_rain: "in the rain",
    modifiers.specific_time: [
        "Saturday night",
        "Tuesday morning",
    ],
}

speech_patterns = [
    "Say,", # Start sentences with this when trying to persuade someone
]

# Given story_state, prose used so far, and potential next beats,
# Return prose for those next beats
#
# Could do tricks like, any common prefixes to the next sets of prose can be
# printed out as normal and then the choices start at the differences. Ending a 
# sentence and staring a new paragraph is probably a pretty common prefix.

# Question - How much out of order output can happen? Would the next beat
# possibly want to modify a paragraph that was already output?
#
# Answer - I think the only way this will work is if each beat can be described
# in order. If that means having a sentence end in the middle and then making a
# choice that's ok, but we can't require describing one beat before another for
# the prose output to sound good. That would have to be encoded into the beat
# conditions in that system.

# Question - Should we look at the full story state? Should we look for specific
# other concepts established earlier? Or should we just look at simple action/
# descripion/tone data? That would mabey imply removing story_state from the
# inputs.

num_sentences_in_paragraph = 4

def get_text(text_data, expr_id):
    text = text_data[expr_id]
    if isinstance(text, list):
        #TODO: smarter logic to not repeat the same one too much
        return random.choice(text)
    return text

class ProseState:
    def __init__(self):
        self.num_sentences_left_till_next_paragraph = num_sentences_in_paragraph

    def append_debug(self, message):
        output = ""
        if self.num_sentences_left_till_next_paragraph != num_sentences_in_paragraph:
            output += "\n" # Jump out because we are in the middle of a paragraph
        output += message + "\n"
        return output

    #TODO: should rename this to be parameterized expressions or introduce another
    # layer to convert them first.
    def append(self, expressions, arguments):
        # TODO: any logic about varying word choice and such

        output = ''

        for expression in expressions:
            is_quote = False #TODO: convert "say" actions to quotations
            if (is_quote or self.num_sentences_left_till_next_paragraph == 0):
                separator = "\n\n"
                self.num_sentences_left_till_next_paragraph = num_sentences_in_paragraph
            else:
                separator = ' '

            #TODO use actual different rules for action and description
            if expression.action_id in actions_text:
                formatted_string = prose.format(
                    get_text(actions_text, expression.action_id), arguments
                )
            elif expression.action_id in descriptions_text:
                formatted_string = prose.format(
                    get_text(descriptions_text, expression.action_id), arguments
                )
            else:
                formatted_string = "ERROR unknown ID: " + expression.action_id

            #TODO: if we just emitted a quote from the same speaker, just
            # continue that in the same paragraph, only closing the quotation
            # marks when we switch to description or another speaker.

            if is_quote:
                assert speaker_param in arguments, (
                    str(speaker_param) + " not in " + str(arguments) +
                    " for " + str(expression.action_id)
                )
                speaker = arguments[speaker_param]
                formatted_string = (
                    '"' + formatted_string + '" said ' + speaker.name
                )

            output += separator + formatted_string
            self.num_sentences_left_till_next_paragraph -= 1

        return output

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

"""
"Is that you, Jake?"
He closed then latched the door behind him. Turning to put his hat on the hook
he replied, "Hey Ma".
"Jake can you come over here". Her voice was feeble.
"I'm working on a case, Ma. I'll talk to you later"
"Jakey wait..."
He had shut the door to his bedroom and did not hear the end of the sentence.
"""

"""
On the right a door was ajar. Miss Ohare walked right passed it to the end of
the hall. "This is his study" she said, ushering him in.
Papers were strewn about the desk. Jake stepped over and started to pick one up.
He heard a muffled voice and turned around. Miss Ohare had left the room. Jake
heard curt speach and then a door click shut. Miss Ohare returned to the room.
"What was that?" asked Jake
"I realized I forgot to shut a window in the other room, that's all."
"""
