import unittest
import story
import main

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

        self.assertTrue(main.is_established_by(concept, idea, {}))
        self.assertFalse(main.is_established_by(concept2, idea, {}))

        argument = 'woo'

        parameterized_concept = story.Concept(['blah'])
        idea_with_arg = main.EstablishedIdea(parameterized_concept, [argument])

        self.assertTrue(main.is_established_by(parameterized_concept, idea_with_arg, {}))
        self.assertTrue(main.is_established_by(parameterized_concept, idea_with_arg, {
            parameterized_concept.parameters[0]:argument,
        }))
        self.assertFalse(main.is_established_by(parameterized_concept, idea_with_arg, {
            parameterized_concept.parameters[0]:'yoyoyo',
        }))

if __name__ == '__main__':
    unittest.main()
