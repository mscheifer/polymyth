import unittest
import random

import util
import story
import story_state

charParam = "c"
chars = ["charA","charB","charC"]
free_arguments = {charParam: chars}

class Test(unittest.TestCase):

    def test_has_duplicates(self):
        self.assertTrue(util.has_duplicates([1,2,2]))
        self.assertTrue(util.has_duplicates([4,4]))
        self.assertFalse(util.has_duplicates([7,99]))
        self.assertFalse(util.has_duplicates([203]))
        self.assertFalse(util.has_duplicates([]))

    def test_is_established_by(self):
        concept = story.Concept([])
        concept2 = story.Concept([])
        idea = story_state.EstablishedIdea(concept, (), ())

        # Idea of concept establishes it
        self.assertTrue(story_state.is_established_by(concept(), idea, {}))
        # Idea of different concept does not
        self.assertFalse(story_state.is_established_by(concept2(), idea, {}))

        argument = 'woo'

        concept_with_param = story.Concept(['blah'])
        idea_with_arg = story_state.EstablishedIdea(concept_with_param, (argument,), ())

        # In a context where the parameter is bound, idea of concept with the same parameter
        # establishes the concept.
        self.assertTrue(story_state.is_established_by(
            concept_with_param(0), idea_with_arg, { 0:argument }
        ))
        # In a context where the parameter is bound, idea of concept with a different parameter
        # does not establish the concept.
        self.assertFalse(story_state.is_established_by(
            concept_with_param(0), idea_with_arg, { 0:'yoyoyo' }
        ))

    def test_try_is_established_and_bind(self):
        argument = 'woo'

        concept_with_param = story.Concept(['blah'])
        idea_with_arg = story_state.EstablishedIdea(concept_with_param, (argument,), ())
        # In a context where the parameter is free, idea of concept with a parameter establishes
        # the concept (and the parameter should be bound afterwards)
        bound_params = {}
        self.assertTrue(story_state.try_is_established_and_bind(
            concept_with_param(0), idea_with_arg, bound_params)
        )
        self.assertEqual(bound_params, {0:argument})

    def test_try_update_with_beat(self):
        concept = story.Concept([])
        concept2 = story.Concept([])

        beat = story.MakeBeat('a').sets_up(concept)

        state = story_state.StoryState(free_arguments)

        # A story beat with no requirements can be used even with no pre-established ideas.
        self.assertIsNotNone(state.try_update_with_beat(beat))

        beatWithReq = story.MakeBeat('b').ok_if(concept2).sets_up(concept)

        self.assertIsNone(state.try_update_with_beat(beatWithReq))

        prohibitedBeat = story.MakeBeat('c').if_not(concept2).sets_up(concept)

        state = story_state.StoryState(free_arguments)
        idea = story_state.EstablishedIdea(concept2, (), ())
        state.established_ideas[idea.get_key()] = idea

        self.assertIsNone(state.try_update_with_beat(prohibitedBeat))

        # TODO: test an exclusive and non-exclusive output concept together, that is definitely
        # broken

    def test_try_update_with_beat__linked_reqs(self):
        concept = story.Concept([])

        linkedConceptA = story.Concept([charParam])
        linkedConceptB = story.Concept([charParam])
        linkedConceptC = story.Concept([charParam])

        state = story_state.StoryState(free_arguments)
        idea1 = story_state.EstablishedIdea(linkedConceptA, (chars[0],), ())
        idea2 = story_state.EstablishedIdea(linkedConceptB, (chars[0],), ())
        idea3 = story_state.EstablishedIdea(linkedConceptC, (chars[0],), ())
        state.established_ideas[idea1.get_key()] = idea1
        state.established_ideas[idea2.get_key()] = idea2
        state.established_ideas[idea3.get_key()] = idea3

        beatWithLinkedReqs = (story.MakeBeat('b')
             .ok_if(linkedConceptA(0), linkedConceptB(0), linkedConceptC(0))
             .sets_up(concept)
        )

        self.assertIsNotNone(state.try_update_with_beat(beatWithLinkedReqs))

    def test_try_update_with_beat__multiple_possilbe_bound_args(self):
        concept = story.Concept([charParam], "c1")
        concept2 = story.Concept([charParam], "c2")
        concept3 = story.Concept([], "c3")

        state = story_state.StoryState(free_arguments)
        idea1 = story_state.EstablishedIdea(concept, (chars[0],), ())
        idea2 = story_state.EstablishedIdea(concept, (chars[1],), ())
        idea3 = story_state.EstablishedIdea(concept2, (chars[0],), ())
        state.established_ideas[idea1.get_key()] = idea1
        state.established_ideas[idea2.get_key()] = idea2
        state.established_ideas[idea3.get_key()] = idea3

        beat = (story.MakeBeat('b')
             .ok_if(concept(0))
             .if_not(concept2(0))
             .sets_up(concept3)
        )
        
        self.assertIsNotNone(state.try_update_with_beat(beat))

    def test_try_update_with_beat__prohibited_linked_to_output(self):
        concept = story.Concept([charParam], "c1")
        concept2 = story.Concept([charParam], "c2")

        state = story_state.StoryState(free_arguments)
        idea = story_state.EstablishedIdea(concept, (chars[0],), ())
        state.established_ideas[idea.get_key()] = idea

        beat = (story.MakeBeat('b')
             .if_not(concept(0))
             .sets_up(concept2(0))
        )

        self.assertIsNotNone(state.try_update_with_beat(beat))

    def test_try_update_with_beat__same_requirement_different_args(self):
        concept = story.Concept([charParam], "c1")
        concept2 = story.Concept([], "c2")

        state = story_state.StoryState(free_arguments)
        idea1 = story_state.EstablishedIdea(concept, (chars[0],), ())
        idea2 = story_state.EstablishedIdea(concept, (chars[1],), ())
        state.established_ideas[idea1.get_key()] = idea1
        state.established_ideas[idea2.get_key()] = idea2

        beat = (story.MakeBeat('b')
             .ok_if(concept(0), concept(1))
             .sets_up(concept2())
        )

        self.assertIsNotNone(state.try_update_with_beat(beat))

    def test_try_update_with_beat__alternative_requirements(self):
        concept = story.Concept([charParam], "ca1")
        concept2 = story.Concept([charParam], "ca2")
        concept3 = story.Concept([charParam], "ca2")

        state = story_state.StoryState(free_arguments)
        idea = story_state.EstablishedIdea(concept, (chars[0],), ())
        state.established_ideas[idea.get_key()] = idea

        beat = (story.MakeBeat('ba')
             .ok_if(concept(0))
             .ok_if(concept2(0))
             .sets_up(concept3(0))
        )

        self.assertIsNotNone(state.try_update_with_beat(beat))

    def test_try_update_with_beat__prohibited_any(self):
        concept = story.Concept([charParam], "ca1")
        concept2 = story.Concept([charParam], "ca2")
        concept3 = story.Concept([], "ca3")

        state = story_state.StoryState(free_arguments)
        # It shouldn't get confused and not look at the next idea of the
        # same concept
        idea1 = story_state.EstablishedIdea(concept, (chars[0],), ())
        idea2 = story_state.EstablishedIdea(concept, (chars[1],), ())
        idea3 = story_state.EstablishedIdea(concept2, (chars[1],), ())
        state.established_ideas[idea1.get_key()] = idea1
        state.established_ideas[idea2.get_key()] = idea2
        state.established_ideas[idea3.get_key()] = idea3

        beat = (story.MakeBeat('ba')
             .if_not(concept(story.any1), concept2(story.any1))
             .sets_up(concept3)
        )

        self.assertIsNone(state.try_update_with_beat(beat))

        state = story_state.StoryState(free_arguments)
        idea1 = story_state.EstablishedIdea(concept, (chars[0],), ())
        idea2 = story_state.EstablishedIdea(concept2, (chars[1],), ())
        state.established_ideas[idea1.get_key()] = idea1
        state.established_ideas[idea2.get_key()] = idea2

        # Should work if the ideas have different args
        self.assertIsNotNone(state.try_update_with_beat(beat))

if __name__ == '__main__':
    random.seed(1234) # for deterministic tests
    unittest.main()
