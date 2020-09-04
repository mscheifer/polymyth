from collections import namedtuple
import enum
import re

# Text is a formatted string. Each format specifier starts with a % sign. There
# is a parameter name, and then a series of letters describing which form of the
# argument will be inserted.
#
# Examples:
# %person:s means to insert the 'person' argument in the posessive case.
# %client:o means to insert the 'client' argument in the object case.
#
# The full list is:
#   s - subject
#   o - object
#   p - posessive
#   v - vocative
#   fv - formal vocative
#   uv - unknown vocative (when the character's name is unknown to the speaker)

@enum.unique
class Case(enum.Enum):
    SUBJECTIVE = 'subject'
    OBJECTIVE = 'object'
    POSESSIVE = 'possessive'
    VOCATIVE = 'vocative'
    FORMAL_VOCATIVE = 'formal-vocative'
    UNKOWN_VOCATIVE = 'unknown-vocative'

ParameterChunk = namedtuple('ParameterChunk', 'case parameter')

pattern = re.compile(r'(%\w+:.)')

def parse(formatted_text):
    split = pattern.split(formatted_text)

    chunks = []
    current_chunk = ""
    for part in split:
        if part.startswith('%') and ':' in part:
            colonIndex = part.index(":", 1) # starting from second character
            # arg name is starting from second character up to colon (non
            # inclusive)
            parameterName = part[1:colonIndex]

            assert len(parameterName) != 0, (
                "can't have empty argument name for: " + part + " in " +
                formatted_text
            )

            # part of speech is after colon and is only one character
            part_of_speach = part[colonIndex + 1 : colonIndex + 2]

            if part_of_speach == "s":
                case = Case.SUBJECTIVE
            elif part_of_speach == "o":
                case = Case.OBJECTIVE
            elif part_of_speach == "p":
                case = Case.POSESSIVE
            elif part_of_speach == "v":
                case = Case.VOCATIVE
            elif part_of_speach == "fv":
                case = Case.FORMAL_VOCATIVE
            elif part_of_speach == "uv":
                case = Case.UNKNOWN_VOCATIVE
            else:
                assert False, (
                    "unknown specifier: " + part + " decomposed as " +
                    parameterName + " " + part_of_speach
                )

            if len(current_chunk) > 0:
                chunks.append(current_chunk)
            chunks.append(ParameterChunk(case, parameterName))

            # Add back anything after the format specifier without a space
            # separating, likely punctuation
            current_chunk = part[colonIndex + 2:]
        else:
            current_chunk += part

    if len(current_chunk) > 0:
        chunks.append(current_chunk)

    return chunks

