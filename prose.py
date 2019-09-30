from collections import namedtuple

# Text is a formatted string. Each format specifier starts with a % sign. There
# is a parameter name (often a number), and then a series of letters describing
# which part of the argument will be inserted.
# %0:n: means to insert the full name of the first argument.
# %2:op: means to insert the object pronoun of the second argument.
# The full list is:
#   n - name
#   sp - subject pronoun
#   op - object pronoun
#   pp - posessive pronoun

# TODO: renmove name and change to just "subject, object, possessive", then let
# the prose state determine whether to use the character's name or a pronoun

_auto_inc_id = 1

def _get_id():
    global _auto_inc_id
    _auto_inc_id += 1
    return _auto_inc_id

introduce_pi = _get_id()
pi_on_phone = _get_id()
what_are_you_up_to_this_weekend = _get_id()
just_some_spring_cleaning = _get_id()
needs_to_help_mom = _get_id()
ask_out_dinner = _get_id()
pi_rejected = _get_id()
pi_phone_fight_waiter = _get_id()
pi_phone_cocky = _get_id()
pi_phone_ask_out_after_many_dates = _get_id()
pi_rejected = _get_id()
client_walks_in = _get_id()
pi_met_client_and_father_once_and_pi_admire_father = _get_id()
father_missing_case = _get_id()
pi_doesnt_take_confident_client_seriously = _get_id()
father_not_at_san_diego_house_awkward_pi = _get_id()
pi_takes_the_case = _get_id()
awkward_pi_confident_client_fees_and_go_to_client_house = _get_id()
i_stopped_caring_what_people_think = _get_id()
rolled_their_eyes = _get_id()
looked_hurt = _get_id()
walks_home_sees_shadows = _get_id()
takes_gun_out_of_desk = _get_id()

opened_shop_late_at_night = _get_id()
served_late_night_customers = _get_id()

father_was_dishonest = _get_id()

Character = namedtuple('Character', 'subject_pronoun object_pronoun possessive_pronoun name')

# If speaker is not None this sentence should be rendered as a quotation.
Sentence = namedtuple('Sentence', 'text_id speaker')

def format(formatted_text, arguments):
    words = formatted_text.split(" ")
    new_words = []
    for word in words:
        to_append = word
        if word.startswith("%") and len(word) > 2:
            colonIndex = word.index(":", 1) # starting from second character
            # arg name is starting from second character up to colon (non inclusive)
            argumentName = word[1:colonIndex]
            secondColonIndex = word.index(":", colonIndex+1)
            # part of speech is between colons
            part_of_speach = word[colonIndex + 1 : secondColonIndex]

            assert argumentName in arguments, (
                argumentName + " not passed in for: " + formatted_text
            )

            if part_of_speach == "n":
                to_append = arguments[argumentName].name
            elif part_of_speach == "sp":
                to_append = arguments[argumentName].subject_pronoun
            elif part_of_speach == "op":
                to_append = arguments[argumentName].object_pronoun
            elif part_of_speach == "pp":
                to_append = arguments[argumentName].possessive_pronoun
            else:
                assert False, ("unknown specifier: " + part_of_speach + " " +
                    str(len(part_of_speach)))

            # Add back anything after the format specifier, likely punctuation
            to_append += word[secondColonIndex+1:]

        new_words.append(to_append)

    return " ".join(new_words)
