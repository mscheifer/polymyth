#!/usr/bin/python3.8
import collections
import random
import unittest

import prose
import story
import story_state

objects = [story.Object("charA"), story.Object("charB"), story.Object("charC")]

content_pack = story.ContentPack(objects, [], [], {})

TestCharacter = collections.namedtuple("TestCharacter", "subject_case")

class Test(unittest.TestCase):

    def test_parse(self):
        parsed = prose.parse("%person:s is here")

        self.assertEqual([
            prose.ParameterChunk(prose.Case.SUBJECTIVE, "person"),
            " is here",
        ], parsed)

    def test_is_established_by(self):
        concept = story.Concept(0)
        concept2 = story.Concept(0)
        idea = story_state.EstablishedIdea(concept, (), ())
        ideas = {idea.get_key(): idea}

        # Idea of concept establishes it
        self.assertTrue(story_state.is_established_by(concept(), ideas, {}))
        # Idea of different concept does not
        self.assertFalse(story_state.is_established_by(concept2(), ideas, {}))

        argument = 'woo'

        concept_with_param = story.Concept(1)
        idea_with_arg = story_state.EstablishedIdea(concept_with_param, (argument,), ())
        ideas_with_arg = {idea_with_arg.get_key(): idea_with_arg}

        # In a context where the parameter is bound, idea of concept with the same parameter
        # establishes the concept.
        self.assertTrue(story_state.is_established_by(
            concept_with_param(0), ideas_with_arg, { '0':argument }
        ))
        # In a context where the parameter is bound, idea of concept with a different parameter
        # does not establish the concept.
        self.assertFalse(story_state.is_established_by(
            concept_with_param(0), ideas_with_arg, { '0':'yoyoyo' }
        ))
        # In a context where the parameter is mapped to a concret object, idea of
        # a concept with the same concrete object establishes the concept.
        obj = story.Object()
        idea_with_object = story_state.EstablishedIdea(concept_with_param, (obj,), ())
        ideas_with_object = {idea_with_object.get_key(): idea_with_object}
        self.assertTrue(story_state.is_established_by(
            concept_with_param(obj), ideas_with_object, {}
        ))
        # In a context where the parameter is mapped to a concret object, idea of
        # a concept with a different concrete object does notestablishes the concept.
        self.assertFalse(story_state.is_established_by(
            concept_with_param(story.Object()), ideas_with_object, {}
        ))

    def test_is_established_by__value_parameters(self):
        argument = 'woo'

        concept_with_param = story.Concept(0, num_value_parameters=1)
        idea_with_arg = story_state.EstablishedIdea(concept_with_param, (), (argument,))
        ideas_with_arg = {idea_with_arg.get_key(): idea_with_arg}

        # In a context where the parameter is bound, idea of concept with the same parameter
        # establishes the concept.
        self.assertTrue(story_state.is_established_by(
            concept_with_param.current([], [0]), ideas_with_arg, { '0':argument }
        ))
        # In a context where the parameter is bound, idea of concept with a different parameter
        # does not establish the concept.
        self.assertFalse(story_state.is_established_by(
            concept_with_param.current([], [0]), ideas_with_arg, { '0':'yoyoyo' }
        ))
        # In a context where the parameter is mapped to a concret object, idea of
        # a concept with the same concrete object establishes the concept.
        obj = story.Object()
        idea_with_object = story_state.EstablishedIdea(concept_with_param, (), (obj,))
        ideas_with_object = {idea_with_object.get_key(): idea_with_object}
        self.assertTrue(story_state.is_established_by(
            concept_with_param.current([], [obj]), ideas_with_object, {}
        ))
        # In a context where the parameter is mapped to a concret object, idea of
        # a concept with a different concrete object does notestablishes the concept.
        self.assertFalse(story_state.is_established_by(
            concept_with_param.current([], [story.Object()]), ideas_with_object, {}
        ))

    def test_try_is_established_and_bind(self):
        argument = 'woo'

        concept_with_param = story.Concept(1)
        idea_with_arg = story_state.EstablishedIdea(concept_with_param, (argument,), ())
        # In a context where the parameter is free, idea of concept with a parameter establishes
        # the concept (and the parameter should be bound afterwards)
        bound_params = {}
        self.assertTrue(story_state.try_is_established_and_bind(
            concept_with_param(0), idea_with_arg, bound_params)
        )
        self.assertEqual(bound_params, {'0':argument})

    def test_try_update_with_beat(self):
        concept = story.Concept(0)
        concept2 = story.Concept(0)

        beat = story.MakeBeat('a').sets_up(concept)

        state = story_state.StoryState([content_pack])

        # A story beat with no requirements can be used even with no pre-established ideas.
        self.assertIsNotNone(state.try_update_with_beat(beat))

        beatWithReq = story.MakeBeat('b').ok_if(concept2).sets_up(concept)

        self.assertIsNone(state.try_update_with_beat(beatWithReq))

        prohibitedBeat = story.MakeBeat('c').if_not(concept2).sets_up(concept)

        state = story_state.StoryState([content_pack])
        idea = story_state.EstablishedIdea(concept2, (), ())
        state.established_ideas[idea.get_key()] = idea

        self.assertIsNone(state.try_update_with_beat(prohibitedBeat))

    def test_try_update_with_beat__linked_reqs(self):
        concept = story.Concept(0)

        linkedConceptA = story.Concept(1)
        linkedConceptB = story.Concept(1)
        linkedConceptC = story.Concept(1)

        state = story_state.StoryState([content_pack])
        idea1 = story_state.EstablishedIdea(linkedConceptA, (objects[0],), ())
        idea2 = story_state.EstablishedIdea(linkedConceptB, (objects[0],), ())
        idea3 = story_state.EstablishedIdea(linkedConceptC, (objects[0],), ())
        state.established_ideas[idea1.get_key()] = idea1
        state.established_ideas[idea2.get_key()] = idea2
        state.established_ideas[idea3.get_key()] = idea3

        beatWithLinkedReqs = (story.MakeBeat('b')
             .ok_if(linkedConceptA(0), linkedConceptB(0), linkedConceptC(0))
             .sets_up(concept)
        )

        self.assertIsNotNone(state.try_update_with_beat(beatWithLinkedReqs))

    def test_try_update_with_beat__multiple_possilbe_bound_args(self):
        concept = story.Concept(1, "c1")
        concept2 = story.Concept(1, "c2")
        concept3 = story.Concept(0, "c3")

        state = story_state.StoryState([content_pack])
        idea1 = story_state.EstablishedIdea(concept, (objects[0],), ())
        idea2 = story_state.EstablishedIdea(concept, (objects[1],), ())
        idea3 = story_state.EstablishedIdea(concept2, (objects[0],), ())
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
        concept = story.Concept(1, "c1")
        concept2 = story.Concept(1, "c2")

        state = story_state.StoryState([content_pack])
        idea = story_state.EstablishedIdea(concept, (objects[0],), ())
        state.established_ideas[idea.get_key()] = idea

        beat = (story.MakeBeat('b')
             .if_not(concept(0))
             .sets_up(concept2(0))
        )

        self.assertIsNotNone(state.try_update_with_beat(beat))

    def test_try_update_with_beat__same_requirement_different_args(self):
        concept = story.Concept(1, "c1")
        concept2 = story.Concept(0, "c2")

        state = story_state.StoryState([content_pack])
        idea1 = story_state.EstablishedIdea(concept, (objects[0],), ())
        idea2 = story_state.EstablishedIdea(concept, (objects[1],), ())
        state.established_ideas[idea1.get_key()] = idea1
        state.established_ideas[idea2.get_key()] = idea2

        beat = (story.MakeBeat('b')
             .ok_if(concept(0), concept(1))
             .sets_up(concept2())
        )

        self.assertIsNotNone(state.try_update_with_beat(beat))

    def test_try_update_with_beat__alternative_requirements(self):
        concept = story.Concept(1, "ca1")
        concept2 = story.Concept(1, "ca2")
        concept3 = story.Concept(1, "ca2")

        state = story_state.StoryState([content_pack])
        idea = story_state.EstablishedIdea(concept, (objects[0],), ())
        state.established_ideas[idea.get_key()] = idea

        beat = (story.MakeBeat('ba')
             .ok_if(concept(0))
             .ok_if(concept2(0))
             .sets_up(concept3(0))
        )

        self.assertIsNotNone(state.try_update_with_beat(beat))

    def test_try_update_with_beat__prohibited_any(self):
        concept = story.Concept(1, "ca1")
        concept2 = story.Concept(1, "ca2")
        concept3 = story.Concept(0, "ca3")

        state = story_state.StoryState([content_pack])
        # It shouldn't get confused and not look at the next idea of the
        # same concept
        idea1 = story_state.EstablishedIdea(concept, (objects[0],), ())
        idea2 = story_state.EstablishedIdea(concept, (objects[1],), ())
        idea3 = story_state.EstablishedIdea(concept2, (objects[1],), ())
        state.established_ideas[idea1.get_key()] = idea1
        state.established_ideas[idea2.get_key()] = idea2
        state.established_ideas[idea3.get_key()] = idea3

        beat = (story.MakeBeat('ba')
             .if_not(concept(story.any1), concept2(story.any1))
             .sets_up(concept3)
        )

        self.assertIsNone(state.try_update_with_beat(beat))

        state = story_state.StoryState([content_pack])
        idea1 = story_state.EstablishedIdea(concept, (objects[0],), ())
        idea2 = story_state.EstablishedIdea(concept2, (objects[1],), ())
        state.established_ideas[idea1.get_key()] = idea1
        state.established_ideas[idea2.get_key()] = idea2

        # Should work if the ideas have different args
        self.assertIsNotNone(state.try_update_with_beat(beat))

    def test_try_update_with_beat__value_objects(self):
        concept = story.Concept(0, num_value_parameters=1)

        state = story_state.StoryState([content_pack])
        state.establish_idea(concept.current([], [objects[0]]), {})

        beat = (story.MakeBeat('b')
             .ok_if(concept.current([], [objects[0]]))
             .sets_up(story.Concept(0))
        )
        self.assertIsNotNone(state.try_update_with_beat(beat))

        beat2 = (story.MakeBeat('b2')
             .ok_if(concept.current([], [objects[1]]))
             .sets_up(story.Concept(0))
        )
        self.assertIsNone(state.try_update_with_beat(beat2))

    def test_try_update_with_beat__are_different(self):
        concept = story.Concept(1, "c1")
        concept2 = story.Concept(1, "c2")
        o_concept = story.Concept(2, "oc1")
        o_concept2 = story.Concept(2, "oc2")

        state = story_state.StoryState([content_pack])
        state.establish_idea(concept(objects[0]), {})
        state.establish_idea(concept2(objects[0]), {})

        beat = (story.MakeBeat('b')
             .ok_if(concept(1), story.are_different(1,2))
             .sets_up(o_concept(1,2))
        )
        self.assertIsNotNone(state.try_update_with_beat(beat))

        beat2 = (story.MakeBeat('b2')
             .ok_if(concept(1), concept2(2))
             .if_not(story.are_different(1,2))
             .sets_up(o_concept2(1,2))
        )
        self.assertIsNotNone(state.try_update_with_beat(beat2))

if __name__ == '__main__':
    random.seed(1234) # for deterministic tests
    unittest.main()
