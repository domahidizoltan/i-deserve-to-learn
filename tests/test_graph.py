from unittest import TestCase
from common.model import Node
from graph import \
    breadth_first_search_in_graph as BFS, \
    minimum_trials_to_reach_from_source_to_destination_word as trials


class GraphTest(TestCase):

    def test_breadth_first_search_in_graph(self):
        n5 = Node(5)
        n3 = Node(3, [n5])
        n4 = Node(4, [n5])
        n2 = Node(2)
        n1 = Node(1, [n2, n3, n4])
        n0 = Node(0, [n1, n2])

        actual_result = BFS.is_path_between(n0, n5)
        self.assertEqual(True, actual_result)

    def test_minimum_trials_to_reach_from_source_to_destination_word(self):
        dictionary = ["BCCI", "AICC", "ICC", "CCI", "MCC", "MCA", "ACC"]
        actual_result = trials.minimum_trials("AICC", "MCA", dictionary)
        self.assertEqual(3, actual_result)
