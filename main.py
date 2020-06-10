#!/usr/bin/python3.8

import itertools
import pprint
import random
import sys

import beats.noir
import english
import story
import story_state

if __name__ == '__main__':
    state = story_state.StoryState([beats.noir.content_pack])
    prose_state = english.ProseState()

    stillTelling = True

    is_debug = len(sys.argv) > 1 and sys.argv[1] == "-d"

    while stillTelling:
        bound_arguments = None
        narrative_piece = None
        
        #TODO: move this logic into story state, or put content pack logic
        #separated somewhere else but this should be with that.
        pieces = beats.noir.narrative_pieces.copy()
        random.shuffle(pieces)
        for piece in pieces:

            expressions_and_debug_output = state.try_update_with_beat(piece)

            if expressions_and_debug_output is not None:
                narrative_piece = piece
                break
        if narrative_piece is None:
            print("\n\nerror no next narrative piece found")
            stillTelling = False
        else:
            expressions, debug_output = expressions_and_debug_output

            if is_debug:
                incremental_output = prose_state.append_debug(
                    pprint.pformat(narrative_piece)
                )
                for debug_out in debug_output:
                    incremental_output += prose_state.append_debug(debug_out)
            elif len(expressions) == 0:
                incremental_output = prose_state.append_debug(
                    "==NO EXP: " + pprint.pformat(narrative_piece) + "=="
                )
            else:
                incremental_output = prose_state.append(expressions)
            print(incremental_output, sep='', end='')
            for parameterized_concept in narrative_piece.parameterized_output_concepts:
                if parameterized_concept.concept is story.story_end:
                    stillTelling = False

    #TODO: refactor this to track concepts generated from each beat, and then
    #track beats that did not lead to anything, as in, at least once concept set
    #up by the beat lead somewhere.
    for unused_idea in story_state.get_ideas_that_have_lead_nowhere(
        state.established_ideas.values(), state.used_ideas
    ):
        if unused_idea.concept is not story.story_end:
            print("error: unused idea -", unused_idea)
