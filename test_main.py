import unittest
import story
import main
import random

class TestMain(unittest.TestCase):

    def test_has_duplicates(self):
        self.assertTrue(main.has_duplicates([1,2,2]))
        self.assertTrue(main.has_duplicates([4,4]))
        self.assertFalse(main.has_duplicates([7,99]))
        self.assertFalse(main.has_duplicates([203]))
        self.assertFalse(main.has_duplicates([]))

    def test_is_established_by(self):
        concept = story.Concept([])
        concept2 = story.Concept([])
        idea = main.EstablishedIdea(concept, [])

        # Idea of concept establishes it
        self.assertTrue(main.is_established_by(concept, idea, {}))
        # Idea of different concept does not
        self.assertFalse(main.is_established_by(concept2, idea, {}))

        argument = 'woo'

        parameterized_concept = story.Concept(['blah'])
        idea_with_arg = main.EstablishedIdea(parameterized_concept, [argument])

        # In a context where the parameter is free, idea of concept with a parameter establishes
        # the concept (and the parameter should be bound afterwards)
        self.assertTrue(main.is_established_by(parameterized_concept, idea_with_arg, {}))
        # In a context where the parameter is bound, idea of concept with the same parameter
        # establishes the concept.
        self.assertTrue(main.is_established_by(parameterized_concept, idea_with_arg, {
            parameterized_concept.parameters[0]:argument,
        }))
        # In a context where the parameter is bound, idea of concept with a different parameter
        # does not establish the concept.
        self.assertFalse(main.is_established_by(parameterized_concept, idea_with_arg, {
            parameterized_concept.parameters[0]:'yoyoyo',
        }))

    def test_can_beat_be_used(self):
        concept = story.Concept([])
        concept2 = story.Concept([])
        beat = story.MakeBeat('a').sets_up(concept)

        # A story beat with no requirements can be used even with no pre-established ideas.
        self.assertIsNotNone(main.can_beat_be_used(beat, []))

        beatWithReq = story.MakeBeat('b').needs(concept2).sets_up(concept)

        self.assertIsNone(main.can_beat_be_used(beatWithReq, []))

        prohibitedBeat = story.MakeBeat('c').if_not(concept2).sets_up(concept)

        self.assertIsNone(
            main.can_beat_be_used(prohibitedBeat, [main.EstablishedIdea(concept2, [])])
        )

        # TODO: test an exclusive and non-exclusive output concept together, that is definitely
        # broken

    def test_can_beat_be_used__linked_reqs(self):
        concept = story.Concept([])

        linkedConceptA = story.Concept(['c'])
        linkedConceptB = story.Concept(['c'])
        linkedConceptC = story.Concept(['c'])

        beatWithLinkedReqs = (story.MakeBeat('b')
             .needs(linkedConceptA(0), linkedConceptB(0), linkedConceptC(0))
             .sets_up(concept)
        )

        self.assertIsNotNone(
            main.can_beat_be_used(beatWithLinkedReqs, [
                main.EstablishedIdea(linkedConceptA, ['s']),
                main.EstablishedIdea(linkedConceptB, ['s']),
                main.EstablishedIdea(linkedConceptC, ['s']),
            ])
        )

    def test_can_beat_be_used__multiple_possilbe_bound_args(self):
        concept = story.Concept(['param'], "c1")
        concept2 = story.Concept(['param'], "c2")
        concept3 = story.Concept([], "c3")

        established_ideas = [
            main.EstablishedIdea(concept, ['s0']),
            main.EstablishedIdea(concept, ['s1']),
            main.EstablishedIdea(concept2, ['s0']),
        ]

        beat = (story.MakeBeat('b')
             .needs(concept(0))
             .if_not(concept2(0))
             .sets_up(concept3)
        )
        
        self.assertIsNotNone(main.can_beat_be_used(beat, established_ideas))

if __name__ == '__main__':
    random.seed(1234) # for deterministic tests
    unittest.main()
