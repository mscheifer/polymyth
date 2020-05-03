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
                argumentName + " not passed in " + str(arguments) + " for: " +
                formatted_text
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
