# http://www.ideserve.co.in/learn/minimum-trials-to-reach-from-source-to-destination-word

from common.model import Node, Edge

queue = list()
visited = set()


def levenshtein_distance(word1, word2):
    word1_length = len(word1) + 1
    word2_length = len(word2) + 1

    if min(word1_length, word2_length) == 1:
        return max(word1_length, word2_length)

    distance_table = [[i+j for i in range(word1_length)] for j in range(word2_length)]

    for i in range(1, word1_length):
        for j in range(1, word2_length):
            cost = int(word1[i-1] != word2[j-1])
            above = distance_table[j-1][i] + 1
            left = distance_table[j][i-1] + 1
            diagonal = distance_table[j-1][i-1] + cost
            distance_table[j][i] = min(above, left, diagonal)

    return distance_table[j][i]


def create_graph(dictionary):
    graph = {word: Node(word) for word in dictionary}
    edges = []
    for word1 in dictionary:
        for word2 in dictionary:
            if levenshtein_distance(word1, word2) is 1:
                edge = Edge(graph[word1], graph[word2])
                if edge not in edges:
                    Edge.connect_bidirectional(edge)
                    edges.append(edge)

    return graph


def find_node(source, destination, steps):
    global queue, visited
    visited.add(source)

    if source is destination:
        return steps

    if source.nodes:
        add_nodes = [n for n in source.nodes if n not in visited]
        queue.extend(add_nodes)

    while queue:
        node = queue.pop()
        if node not in visited:
            return find_node(node, destination, steps+1)

    return -1


def minimum_trials(source, destination, dictionary):
    graph = create_graph(dictionary)
    return find_node(graph[source], graph[destination], 0)


if __name__ == "__main__":
    dictionary = ["BCCI","AICC","ICC","CCI","MCC","MCA", "ACC"]
    source = "AICC"
    destination = "MCA"

    trials = minimum_trials(source, destination, dictionary)
    print("minimum trials from {} to {}: {}".format(source, destination, trials))
