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

import prose
import english

class ProseState:
    def __init__(self):
        self.num_sentences_left_till_next_paragraph = 0

    #TODO: should rename this to be parameterized sentences or introduce another
    # layer to convert them first.
    def append(self, sentences, arguments):
        # TODO: any logic about varying word choice and such

        output = ''

        for sentence in sentences:
            if (
                sentence.speaker_param is not None or
                self.num_sentences_left_till_next_paragraph == 0
            ):
                separator = "\n\n"
                self.num_sentences_left_till_next_paragraph = 4
            else:
                separator = ' '

            formatted_string = prose.format(
                english.text[sentence.text_id], arguments
            )

            #TODO: if we just emitted a quote from the same speaker, just
            # continue that in the same paragraph, only closing the quotation
            # marks when we switch to description or another speaker.

            if sentence.speaker_param is not None:
                assert sentence.speaker_param in arguments, (
                    str(sentence.speaker_param) + " not in " + str(arguments) +
                    " for " + str(sentence.text_id)
                )
                speaker = arguments[sentence.speaker_param]
                formatted_string = (
                    '"' + formatted_string + '" said ' + speaker.name
                )

            output += separator + formatted_string
            self.num_sentences_left_till_next_paragraph -= 1

        return output
