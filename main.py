import itertools
import pprint
import random
import sys

import prose_state
import beats.noir
import story
import story_state

if __name__ == '__main__':
    state = story_state.StoryState(beats.noir.free_arguments)
    prose_state = prose_state.ProseState()

    print("Begin", end='')

    stillTelling = True

    count = 0

    is_debug = len(sys.argv) > 1 and sys.argv[1] == "-d"

    while stillTelling:
        count = count + 1
        bound_arguments = None
        narrative_piece = None
        
        pieces = beats.noir.narrative_pieces.copy()
        random.shuffle(pieces)
        for piece in pieces:

            args_and_used_ideas = state.try_update_with_beat(piece)

            if args_and_used_ideas is not None:
                narrative_piece = piece
                break
        if narrative_piece is None:
            print("\n\nerror no next narrative piece found")
            stillTelling = False
        else:
            arguments, used_ideas = args_and_used_ideas

            if is_debug or len(narrative_piece.parameterized_sentences) == 0:
                incremental_output = pprint.pformat(
                    (narrative_piece, arguments, used_ideas)
                ) + "\n"
            else:
                incremental_output = prose_state.append(
                    narrative_piece.parameterized_sentences, arguments
                )
            print(incremental_output, sep='', end='')
            for parameterized_concept in narrative_piece.parameterized_output_concepts:
                if parameterized_concept.concept is story.story_end:
                    stillTelling = False

    for unused_idea in story_state.get_ideas_that_have_lead_nowhere(
        state.established_ideas.values(), state.used_ideas
    ):
        if unused_idea.concept is not story.story_end:
            print("error: unused idea -", unused_idea)
