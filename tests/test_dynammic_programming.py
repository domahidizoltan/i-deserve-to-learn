from unittest import TestCase
from dynamic_programming import \
    edit_distance_dynamic_programming as distance, \
    word_break_problem as word_break


class DynamicProgrammingTest(TestCase):

    def test_edit_distance_dynamic_programming(self):
        actual_result = distance.levenshtein_distance('INTENTION', 'EXECUTION')
        self.assertEqual(5, actual_result)

    def test_word_break_problem(self):
        dictionary = ["arrays", "dynamic", "heaps", "IDeserve", "learn", "learning", "linked", "list", "platform",
                      "programming", "stacks", "trees"]
        actual_result = word_break.brake_word("IDeservelearningplatform", dictionary)
        self.assertEqual(True, actual_result)
