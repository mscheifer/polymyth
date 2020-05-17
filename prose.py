from collections import namedtuple
import enum

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
#   v - vocative

@enum.unique
class Case(enum.Enum):
    SUBJECTIVE = 'subject'
    OBJECTIVE = 'object'
    POSESSIVE = 'possessive'
    VOCATIVE = 'vocative'

ParameterChunk = namedtuple('ParameterChunk', 'case parameter')

def parse(formatted_text):
    words = formatted_text.split(" ")
    chunks = []
    current_chunk = ""
    for word in words:
        if word.startswith("%") and len(word) > 2:
            colonIndex = word.index(":", 1) # starting from second character
            # arg name is starting from second character up to colon (non
            # inclusive)
            parameterName = word[1:colonIndex]

            assert len(parameterName) != 0, (
                "can't have empty argument name for: " + word + " in " +
                formatted_text
            )

            # part of speech is after colon and is only one character
            part_of_speach = word[colonIndex + 1 : colonIndex + 2]

            if part_of_speach == "s":
                case = Case.SUBJECTIVE
            elif part_of_speach == "o":
                case = Case.OBJECTIVE
            elif part_of_speach == "p":
                case = Case.POSESSIVE
            elif part_of_speach == "v":
                case = Case.VOCATIVE
            else:
                assert False, (
                    "unknown specifier: " + word + " decomposed as " +
                    parameterName + " " + part_of_speach
                )

            if len(current_chunk) > 0:
                chunks.append(current_chunk + " ")
            chunks.append(ParameterChunk(case, parameterName))

            # Add back anything after the format specifier without a space
            # separating, likely punctuation
            current_chunk = word[colonIndex + 2:]
        else:
            current_chunk += " " + word

    if len(current_chunk) > 0:
        chunks.append(current_chunk)

    return chunks

