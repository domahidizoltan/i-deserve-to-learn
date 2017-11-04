# http://www.ideserve.co.in/learn/breadth-first-search-in-graph

from common.model import Node


def is_path_between(source, dest):
    queue = list()
    queue.append(source)
    while queue:
        source = queue.pop(0)
        if source.node_id == dest.node_id:
            return True

        nodes = [node for node in source.nodes]
        queue.extend(nodes)

    return False


if __name__ == "__main__":
    n5 = Node(5)

    n3 = Node(3, [n5])
    n4 = Node(4, [n5])

    n2 = Node(2)
    n1 = Node(1, [n2, n3, n4])

    n0 = Node(0, [n1, n2])

    print("path exists between source and destination: ", is_path_between(n0, n5))
