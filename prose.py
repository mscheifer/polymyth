from collections import namedtuple

# Text is a formatted string. Each format specifier starts with a % sign. There
# is a parameter name (often a number), and then a series of letters describing
# which part of the argument will be inserted.
#
# Examples:
# %0:s means to insert the first argument in the posessive case.
# %2:o means to insert the second argument in the object case.
#
# The full list is:
#   s - subject
#   o - object
#   p - posessive

CasedWord = namedtuple('CasedWord', 'subject_case object_case possessive_case')

def format(formatted_text, arguments):
    assert isinstance(arguments, dict)
    words = formatted_text.split(" ")
    new_words = []
    for word in words:
        to_append = word
        if word.startswith("%") and len(word) > 2:
            colonIndex = word.index(":", 1) # starting from second character
            # arg name is starting from second character up to colon (non
            # inclusive)
            argumentName = word[1:colonIndex]
            # part of speech is after colon and is only one character
            part_of_speach = word[colonIndex + 1 : colonIndex + 2]

            assert argumentName in arguments, (
                argumentName + " not passed in " + str(arguments) + " for: " +
                formatted_text
            )

            if part_of_speach == "s":
                to_append = arguments[argumentName].subject_case
            elif part_of_speach == "o":
                to_append = arguments[argumentName].object_case
            elif part_of_speach == "p":
                to_append = arguments[argumentName].possessive_case
            else:
                assert False, (
                    "unknown specifier: " + word + " decomposed as " +
                    argumentName + " " + part_of_speach
                )

            # Add back anything after the format specifier without a space
            # separating, likely punctuation
            to_append += word[colonIndex + 2:]

        new_words.append(to_append)

    return " ".join(new_words)
