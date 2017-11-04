from unittest import TestCase
from strings import \
    group_all_anagrams_together_set_1 as anagram_groups, \
    longest_substring_with_non_repeating_characters as non_repeating_substring, \
    postfix_expression_evaluation as postfix, \
    remove_spaces_from_string as spaces


class StringsTest(TestCase):

    def test_group_all_anagrams_together_set_1(self):
        words = ["abcd", "abc", "abce", "acd", "abdc"]
        actual_result = anagram_groups.group_by_anagrams(words)
        expected_result = ['abc', 'abcd', 'abdc', 'abce', 'acd']
        self.assertEqual(expected_result, actual_result)

    def test_longest_substring_with_non_repeating_characters(self):
        actual_result = non_repeating_substring.find_longest_non_repeating_substring("ABCDABDEFGCABD")
        self.assertEqual("ABDEFGC", actual_result)

    def test_postfix_expression_evaluation(self):
        values = ['5', '1', '2', '+', '4', '*', '+', '3', '-']
        actual_result = postfix.postfix_expression_evalutaion(values)
        self.assertEqual('14', actual_result)

    def test_remove_spaces(self):
        actual_result = spaces.remove_spaces("  Hi, How are you?  ")
        self.assertEqual("Hi,Howareyou?", actual_result)
