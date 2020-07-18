from collections import namedtuple
import enum
import random

import expression.actions as actions
import expression.descriptions as descriptions
import expression.humans as humans
import expression.modifiers as modifiers
import expression.nouns as nouns
import prose

# The philosophy here is that the experience will be like Groundhog Day. The
# beat choices will always give the same output, so it's ok if the same text
# appears in the same place in the story every time, or if similar text appears
# there for minor variations. We do want to avoid the same text appearing again
# later in the story though.

todo_use_these = [
    #father_was_dishonest:
    """"My name is Jake Marbery. I believe you used to work with my father Sam Marbury."
    "Oh yes, I remember him. He did _______ work for us for a couple years a few decades back."
    "Yeah he had a _______ business back then."
    "That's true. He may have lied about other things but that was true." """,
]

Quote = namedtuple("Quote", ["speaker", "text", "tag"], defaults=["said"])

actions_text = {
    actions.ask_about_match_book_then_meet_mysterious_woman: [
        Quote("bartender", "What'll it be, friend?"),
        Quote("pi", "Whiskey sour"),
        Quote("bartender", "Coming right up."),
        Quote("pi", "Say, got any matches?"),
        Quote("bartender", "Of course"),
        ("The bartender handed %pi:o a book of matches identical to the one " +
            "from the house."),
        Quote("pi", "Thanks"),
        Quote("ml", "What are you investigating now, %pi:v?"),
        Quote("pi", "%ml:v, why am I not surprised to find you here?"),
        Quote("ml", "Uhh, because I found this bar before you did?"),
        Quote("pi", "Why are you looking for this bar?"),
        Quote("ml", "I'm not looking for this bar I'm just living my life."),
        Quote("ml", "Why are YOU looking for this bar?"),
        Quote("pi", "Nevermind, forget it."),
        Quote("ml", "Come on now. I've been hanging out here for weeks."),
        Quote("ml", "Now that you know that you have to do your due diligence" +
            " and talk to me."),
        "%pi:s eyed %ml:o.",
        Quote("ml", "Come on. I saw you staring at that matchb book lost in " +
            "thought. You forgot to pull out a cigarette. Come tell me who " +
            "you're looking for and I'll tell you if I've seen them."),
        Quote("pi", "Alright, since you asked so nicely."),
        "%ml:s went and sat down at a booth.",
    ],
    actions.ask_how_are_you:
        Quote("person", "How are you?"),
    actions.ask_if_want: (
        "Do you like to",
        "Do you want to",
        "How about we",
        "How would you like to",
        "Would you like to",
        "Would you want to",
    ),
    actions.ask_if_father_left_town: [
        Quote("pi", "Did he go out of town, take a little vacation?"),
        Quote("client", "He would never without telling someone."),
        Quote("pi", "Does he own a summer beach house, somewhere he likes to " +
            "get away?"),
        Quote("client", "Yes, a place in San Diego."),
        Quote("client", "I went there two days ago. He is not there, and " +
            "again, if he went he would have told me."),
        Quote("pi", "Ok, ok. Where did you last see him?"),
        Quote("client", "At the house for breakfast on Thursday."),
        Quote("pi", "I guess we can start there."),
        "%client:s rose from the chair.",
        Quote("client", "Thank you for helping."),
        Quote("client", "I drove my car over here. Follow me?"),
        Quote("pi", "Yes certainly."),
        #TODO: how could I make it so this phrase could be combined with the
        # previous one by the engine to make one sentence out of the action and
        # dialog tag
        "%pi:s got up.",
        Quote("pi", "By the way my fee structure is fourty doll..."),
        Quote("client", "Fourty dollars a day plus expenses."),
        Quote("client", "I read your sign on the door."),
        "%client:s turned and left. %pi:s followed.",
    ],
    actions.ask_to_recount_forgotten_childhood: Quote("person", "Wait, tell " +
        "me about our old friends, after school, running in the park. We " +
        "thought we saw something magical in the woods. I have forgotten " +
        "now, but you might still remember"),
    actions.ask_out_after_many_dates: 
        Quote("person", "That's what I'm saying. You and me, out on the town " +
        "again. That sax player you like is playing again at Charlie's."),
    actions.ask_what_are_you_up_to_this_weekend: 
        Quote("person", "What are you up to this weekend?"),
    actions.ask_why_you_didnt_know_where_from: [
        Quote("person1", "Why don't you know where your friend was from?"),
        Quote("person1", "Didn't he tell you?"),
        Quote("person2", "Some men are ashamed of their beginnings."),
    ],
    actions.avoid_interaction_with_mother: [
        #TODO: there shouldn't be a diaglog tag here even if this is the first
        # line for the mother, because we figure out who it is from the next line.
        Quote("mother", "Is that you, %pi:v?"),
        "He closed then latched the door behind him.",
        "He turned to put his hat on the hook.",
        Quote("pi", "Hey Ma", tag="replied"),
        Quote("mother", "%pi:v can you come over here"),
        "%mother:p voice was feeble.", # TODO: way to have this grouped with previous line?
        Quote("pi", "I'm working on a case, Ma. I'll talk to you later"),
        Quote("mother", "%pi:v wait..."), #TODO: use diminuitive name like "jakey" for "jake"
        ("He had shut the door to his bedroom and did not hear the end of the " +
            "sentence."),
    ],
    actions.be_cocky_on_phone: [
        #TODO: diminutive genered noun here instead of always 'girl'
        Quote("pi", "You're real funny, girl. Why don't I come pick you up at" +
        " 7:00."),
        Quote("date", "How about this. Don't call me again until you've found" +
        " some decency."),
        Quote("pi", "Wait what? %date:v?... Hello?"),
        "%:pi:n put the receiver down and twirled his thumbs.",
    ],
    actions.close_ramen_shop: [
        "When the sun started to come up %owner:s locked up and headed out."
    ],
    actions.encounter_sibyl: [
        Quote("sibyl", "I have 3 volumes of meeting notes from your father's " +
            "company."),
        Quote("sibyl", "I know you're digging in and would want to look at " +
            "these."),
        Quote("sibyl", "I'll let you have them for a price."),
        Quote("client", "How much?"),
        Quote("sibyl", "100,000 dollars"),
        Quote("sibyl", "Hell no, I can't afford that. What about 5,000 " +
            "dollars?"),
        Quote("sibyl", "100,000 dollars or no deal"),
        Quote("client", "10,000 but I won't go higher than that."),
        Quote("sibyl", "I'm not budging"),
        Quote("client", "What use are they to you?"),
        Quote("client", "If you don't take my offer you'll have nothing."),
        Quote("sibyl", "...you're right. They're of no use to me."),
        "%sibyl:s took out a lighter and lit the corner of one volume.",
        Quote("client", "What are you doing?"),
        "%sibyl said nothing.",
        "%sibyl dropped the volume on the ground and stamped out the flames " +
            "with her foot.",
        Quote("sibyl", "100,000 dollars for the remaining two volumes"),
        Quote("client", "Hell no"),
        "%sibyl:s took a second volume and lit it.",
        Quote("sibyl", "100,000 dollars for the one remaining volume and " +
            "whatever you can salvage from these two scraps"),
        "The color drained from %client:p face.",
        Quote("client", "OK, Ok, yes stop. I'll pay it."),
    ],
    actions.enters_seedy_bar: [
        "%pi:s approached the un-assuming black door.",
        "%pi:s knocked twice.",
        "A slot opened at head level revealing a man wearing an eye patch.",
        Quote("doorman", "What do you want?"),
        Quote("pi", "Uhh, to come in and have a drink."),
        Quote("doorman", "Do you have your wits about ye?"),
        Quote("pi", "Um... Yes?"),
        Quote("doorman", "Alright come on in."),
    ],
    actions.follow_father_inside_then_meet_mysterious_woman: [
        "The place was almost empty. %pi:s took a quick peak in each booth, " +
        "then he went back and checked the men's bathroom. The father had " +
        "vanished. %pi:s sat down at the bar. %pi:s felt suddenly winded.",
        Quote("pi", "Hey, did you see an old man come in here?"),
        Quote("bartender", "Umm, yeah an old man came in a few hours ago"),
        Quote("pi", "No, I mean just now. I followed him in here."),
        Quote("bartender", "Nah, nobody came in before you."),
        "The bartender gave %pi:o a quizzical look.",
        Quote("pi", "Alright, I must have mistook him for someone else."),
        # TODO: genered causual address
        Quote("bartender", "You want something to drink man?"),
        "%bartender:p kept a neutral expression.",
        Quote("pi", "Uhh, yeah sure. How about a whiskey sour."),
        # TODO: genered causual address
        Quote("bartender", "You got it my man."),
        Quote("ml", "Is this old man in trouble. Does he need you?"),
        # TODO: man / woman
        "%pi:s turned. A woman was similing at him from a booth.",
        Quote("pi", "Maybe. His family seemed to think he's missing."),
        Quote("ml", "But you just saw him."),
        Quote("pi", "I thought so. Well I definitely did but I'm not sure he " +
            "actually came in here. I guess I lost him."),
        Quote("ml", "Here. Come sit and tell me more."),
        Quote("ml", "Nothing has happened all night but this is..."),
        Quote("ml", "Well this is something at least."),
    ],
    actions.get_rejected: [
        Quote("date", "Oh, your going to go help your mom out? That's so " +
        "nice... Well... I don't think I want to see you again. You seemed " +
        "very quiet and uncomfortable around me."),
        Quote("pi", "Wait now, that was just the first date. I was trying to " +
        "be respectful. I can be more... I wasn't uncomfortable."),
        Quote("date", "Anyway, I've got to go. Have a nice weekend."),
        "%pi:s put the receiver down and sat up.",
    ],
    actions.go_home: "%person:s goes home.",
    actions.hang_up: [
        Quote("person", "I gotta go actually, goodbye."),
        "%person:s hung up the phone.",
    ],
    actions.hear_client_father_is_missing: [
        Quote("client", "That's just the thing,"),
        ("%client:s took a cigarette holder from %client:p purse and withdrew" +
        " one, lighting it with a match."),
        Quote("client", "He may be in trouble."),
        Quote("pi", "What kind of trouble?"),
        Quote("client", "I don't know. He hasn't been seen in 3 days."),
    ],
    actions.hear_daughter_has_run_off: [
        Quote("client", "He's alright."),
        Quote("client", "He's spending the long weekend in San Diego."),
        Quote("client", "I've come here to today because I need your help " +
            "before he get's back."),
        Quote("pi", "Before he returns on Monday?"),
        Quote("client", "Yes Monday morning."),
        Quote("client", "My sister is missing."),
        Quote("client", "I know who she is with but not where they are."),
        Quote("client", "If we can find her and bring her back my father " +
            "doesn't need to know about this."),
    ],
    actions.hear_regular_father_is_missing: [
        "%regular:p movements seemed slower than normal, %owner:s noticed.",
        "%owner:s stopped drumming %owner:p fingers.",
        Quote("regular", "Have you seen my dad?", "asked"),
        Quote("owner", "Not for a few weeks."),
        Quote("regular", "Ok, sorry to bother you."),
        Quote("owner", "Is something wrong?"),
        Quote("regular", ("...He didn't come home last night. I'm worried he " +
        "fell down somewhere.")),
        Quote("owner", "Oh, I..."),
        Quote("regular", "Thanks, anyway"),
        "%regular:s turned and left.",
    ],
    actions.join_mysterious_woman: [
        "%pi:s left the bar and took a seat across from the woman",
        # Yeah I usually hang out here and hold court.
    ],
    actions.lean_back_in_chair: ( "%person:s leaned back in %person:p chair and"
        + " propped %person:p legs up on the desk."
    ),
    actions.look_hurt: "%person:s frowned and looked away.",
    actions.look_in_study: [
        "On the right a door was ajar.",
        #TODO: how to have it use formal address like "Miss O'hare" in the
        #descriptive text?
        "%client:s walked right passed it to the end of the hall.",
        Quote("client", "This is his study"),
        "%client:s ushered him in.",
        "Papers were strewn about the desk.",
        "%pi:s stepped over and started to pick one up.",
        "He heard a muffled voice and turned around.",
        "%client:s had left the room.", #Here too
        "%pi:s heard curt speach and then a door click shut.",
        "%client:s returned to the room.",
        Quote("pi", "What was that?"),
        Quote("client", "I realized I forgot to shut a window in the other " +
            "room. That's all."),
    ],
    actions.open_paper: "%person:s cracked open the afternoon Chronicle.",
    actions.read_political_scandal_in_paper:
        "In big bold letters it read: SENATOR WYDEN'S CORRUPT LAND DEAL.",
    actions.roll_eyes: "%person:s rolled their eyes.",
    actions.say_distrust_moderate_drinkers: [
        Quote("person", "I like a man who doesn't say when."),
        Quote("person", "If he's careful not to drink too much then it means " +
            "he's not to be trusted when he does drink"),
    ],
    actions.say_met_client_and_father_once_and_admire_father: [
        Quote("client", "Goodhall, but we have been aquainted before. You " +
        "came to my Father's 60th birthday party 4 years back."),
        Quote("pi", "Ahh... yes of course. Your father was a great man from " +
        "all the stories I had heard and I was glad to meet him. How is he?"),
    ],
    actions.say_needs_to_help_mom: ("I gotta stop by my mom's place at some " +
        "point to help her move a bookcase. But that's about it."),
    actions.say_oh_not_much:
        "Oh not much. Just some spring cleaning. You?",
    actions.say_saw_pi_in_a_dream: [
        Quote("client", "You know. I came to you because I knew you from a " +
            "dream."),
        "%pi:s looked at %client:o.",
        Quote("client", "I dreamed I was riding a horse through the dark of " +
            "night. I was so tired. I saw a fire in the distance and rode for" +
            " it. It was your camp. You shared some beans with me..."),
        Quote("pi", "I was eating a can of beans?"),
        "%pi:s laughed.",
        "%client:s laughed too.",
        Quote("client", "It's silly imagining a city boy eating beans " +
            "straight from a can. But you don't worry about things like that " +
            "in a dream."),
    ],
    actions.say_they_are_happy_just_being_alive_cooly:
        Quote("person", "I'm alive, which is pretty engaging"),
    actions.say_you_can_talk_to_me_about_anything: [
        Quote("person", "You know you can talk to me about anything"),
    ],
    actions.say_you_have_to_drink: [
        Quote("person", "No, you're cheersing wrong. Peoplw who are pregnant," +
            " that's ok. If you don't have a legitamite excuse you should be " +
            "drinking"),
    ],
    actions.see_client_walk_in: [
        ("%pi:s had been drumming %pi:p fingers and staring at the wall when " +
        "%pi:s heard a knock on the door."),
        Quote("pi", "Come on in."),
        Quote("client", "Good evening %pi:v. May I have a seat?"), # TODO: formal vocative case
        Quote("pi", "Please, %client:v"), # TODO: formal vocative unknown name case
        "%pi:s stuck out %pi:p hand.",
    ],
    actions.see_regular_walk_in: [
        ("%owner:s had been drumming %owner:p fingers and staring at the wall "
        + "when %owner:s heard a customer walk in."),
        "It was %regular:o, a regular.",
    ],
    actions.see_shadows_of_people_following:
        "%person:s saw shadows of people following %person:o",
    actions.state_dont_care_what_people_think: ("Maybe that would have shook " +
        "me before I was 10 and stopped caring what people think"),
    actions.take_gun_out_of_desk: [
        "%person:s opened a drawer in %person:p desk.",
        "%person:s withdrew a gun and holstered it under %person:p jacket.",
    ],
    actions.talk_about_fight_waiter: [
        Quote("date", "Are you going to pick a fight with the waiter again? " +
        "I'msurprised you think they'll let you back in the place."),
        Quote("pi", "I think he and I came to an understanding. Even if not, " +
        "wouldn't you want to watch me give him a good one, huh? Right in the" +
        " kisser."),
        Quote("date", "Wow, you're well fixed on this guy. Maybe I should " +
        "give you space to get to know him."),
    ],
    actions.turn_on: "%person:s turned on the %thing:o",
    actions.twirl_phone_cord: "%person:p fingers twirled the phone cord.",
    actions.walk_to: "%person:s walked to %to:o.",
    actions.watch_talk_show_about_ghosting: ("The host was in the middle of " +
        "asking his guest. 'Have you ever ghosted anyone?' 'Well I ghosted my" +
        " guitar teacher.' Canned laughter."),
    actions.writhe_on_ground: "%person:s collapsed and writhed on the ground.",
}

descriptions_text = {
    descriptions.opened_shop_late_at_night:
        "%person:s opened the shop every day at 10 pm and closed it again at 8 am.",
    descriptions.picture_and_last_words: [
        ("It was a nice picture of %partner:o, the one on %person:p desk, but " +
        "%person:s didn't look at it often."),
        ("Everytime %person:s glanced at it %partner:p last words replayed in " +
        "%person:p head."),
        '"Swing away, %person:v, swing away."',
    ],
    descriptions.served_late_night_customers:
        "%person:s served taxi drivers, bar tenders and graveyard shift workers.",
}

nouns_text = {
    nouns.bartender: "bartender",
    nouns.doorman: "doorman",
    nouns.home: "home",
    nouns.on_a_date: (
        "out to dinner",
        "on a date",
    ),
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

num_sentences_in_paragraph = 4

def get_lines(text_data, expr_id):
    text = text_data[expr_id]
    if isinstance(text, tuple):
        #TODO: smarter logic to not repeat the same one too much
        return [random.choice(text)]
    if isinstance(text, list):
        return text
    assert isinstance(text, str)
    return [text]

CasedWord = namedtuple('CasedWord', 'subject_case object_case possessive_case vocative_case')

@enum.unique
class ParagraphSubjects(enum.Enum):
    DESCRIPTION = 'description'
    ACTION = 'action'

class ProseState:
    def __init__(self):
        #TODO: smarter paragraph logic. We want to group related stuff together
        # in the same paragraph and separate out unrelated stuff. How will we
        # know what is related across beats?
        self.num_sentences_left_till_next_paragraph = 0

        self.gender_to_last_character_reffered_to = {
            "male": None, "female": None,
        }
        self.current_speaker = None

        self.current_paragraph_subject = None

    def append_debug(self, message):
        output = ""
        if self.num_sentences_left_till_next_paragraph != num_sentences_in_paragraph:
            output += "\n" # Jump out because we are in the middle of a paragraph
        output += message + "\n"
        return output

    def _get_noun_cased_word_and_update_context(self, noun, unnamed_title):
        def get_raw_noun_string(noun):
            assert noun in nouns_text, (
                str(noun) + " not in map"
            )
            raw_noun = nouns_text[noun]
            if isinstance(raw_noun, tuple):
                #TODO: smarter logic to not repeat the same one too much
                raw_noun = random.choice(raw_noun)
            return raw_noun

        if isinstance(noun, nouns.ProperNoun):
            if noun in humans.men:
                gender = "male"
            elif noun in humans.women:
                gender = "female"
            else:
                assert False, "unknown human object" + str(noun)

            name = (
                noun.raw_name if unnamed_title is None
                else "the " + get_raw_noun_string(unnamed_title)
            )

            if self.gender_to_last_character_reffered_to[gender] is not noun:
                self.gender_to_last_character_reffered_to[gender] = noun
                return CasedWord(name, name, name + "'s", name)
            else:
                if gender == "male":
                    return CasedWord("he", "him", "his", name)
                elif gender == "female":
                    return CasedWord("she", "her", "her", name)
                else:
                    assert False
        raw_noun = get_raw_noun_string(noun)
        return CasedWord(raw_noun, raw_noun, raw_noun + "'s", raw_noun)

    def _format_line(self, formatted_line, argument_map, unnamed_titles):
        prose_chunks = prose.parse(formatted_line.strip())

        sentence = ""
        for chunk in prose_chunks:
            if isinstance(chunk, prose.ParameterChunk):
                noun = argument_map[chunk.parameter]
                unnamed_title = unnamed_titles.get(chunk.parameter) #may be None
                cased_word = self._get_noun_cased_word_and_update_context(
                    noun, unnamed_title
                )
                if chunk.case is prose.Case.SUBJECTIVE:
                    text = cased_word.subject_case
                elif chunk.case is prose.Case.OBJECTIVE:
                    text = cased_word.object_case
                elif chunk.case is prose.Case.POSESSIVE:
                    text = cased_word.possessive_case
                elif chunk.case is prose.Case.VOCATIVE:
                    text = cased_word.vocative_case
                else:
                    assert False, "UNKOWN CASE " + case
            else:
                text = chunk
            sentence += text
        return sentence[0].upper() + sentence[1:]

    def append(self, expressions):
        # TODO: any logic about varying word choice and such

        output = ''

        for expression in expressions:
            if expression.core in actions_text:
                text_map = actions_text
                next_subject = ParagraphSubjects.ACTION
            elif expression.core in descriptions_text:
                text_map = descriptions_text
                next_subject = ParagraphSubjects.DESCRIPTION
            else:
                assert False, "ERROR unknown ID: " + expression.core

            lines = get_lines(text_map, expression.core)
            arguments = expression.argument_map
            unnamed_titles = expression.unnamed
            for line in lines:
                if isinstance(line, Quote):
                    line_string = line.text
                    speaker_param = line.speaker
                    assert speaker_param in arguments, (
                        str(speaker_param) + " not in " + str(arguments) +
                        " for " + line_string
                    )
                    line_string = '"' + line_string + '"'
                    speaker = arguments[speaker_param]
                    #TODO: allow two speakers to alternate without tags for a
                    #short period
                    if self.current_speaker is not speaker:
                        #TODO: we can actually vary the word order here but only
                        # if it's a proper noun. ("she said" and "Sarah said"
                        # are both valid but "said Sarah" is and "said she" is
                        # not.) But we don't know which one we're going to use
                        # here without some refactoring, although if this type
                        # of situation comes up more then we could just make it
                        # part of the formatting language.
                        line_string = " ".join((
                            line_string,
                            "%" + speaker_param + ":s",
                            line.tag + "."
                        ))
                        self.current_speaker = speaker
                else:
                    assert isinstance(line, str)
                    line_string = line
                    speaker = None

                sentence = self._format_line(
                    line_string, arguments, unnamed_titles
                )

                #TODO: I want to interleave descriptive language into pauses in
                #dialog sometimes
                if (
                    speaker is not None or
                    self.num_sentences_left_till_next_paragraph == 0 or
                    next_subject != self.current_paragraph_subject
                ):
                    separator = "\n    "
                    self.num_sentences_left_till_next_paragraph = num_sentences_in_paragraph
                    self.current_paragraph_subject = next_subject
                else:
                    separator = ' '

                output += separator + sentence
                self.num_sentences_left_till_next_paragraph -= 1

        return output

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

