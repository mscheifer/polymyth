import itertools
import random

import noir
import story
import story_state

if __name__ == '__main__':
    state = story_state.StoryState(noir.free_arguments)

    stillTelling = True

    count = 0

    while stillTelling:
        count = count + 1
        bound_arguments = None
        narrative_piece = None
        
        pieces = noir.narrative_pieces.copy()
        random.shuffle(pieces)
        for piece in pieces:

            arguments = state.try_update_with_beat(piece)

            if arguments is not None:
                narrative_piece = piece
                break
        if narrative_piece is None:
            print("error no next narrative piece found")
            stillTelling = False
        else:
            print(narrative_piece, " - ", arguments)
            for output_concept in narrative_piece.output_concepts:
                if output_concept is story.story_end:
                    stillTelling = False

    for unused_idea in get_ideas_that_have_lead_nowhere(
        state.established_ideas, state.used_ideas
    ):
        print("error: unused idea -", unused_idea)
