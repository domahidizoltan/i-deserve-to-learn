class Node(object):

    def __init__(self, node_id, nodes=None):
        self.node_id = node_id
        self.edges = list()
        self.nodes = list()
        if nodes:
            for node in nodes:
                Edge.connect_one_way(Edge(self, node))


    def add_edge(self, edge):
        self.edges.append(edge)
        node = edge.node2 if edge.node1 is self else edge.node1
        self.nodes.append(node)

    def __repr__(self):
        return "[nodeId={}]".format(self.node_id, self.nodes)


class Edge(object):

    def __init__(self, node1, node2, distance=1):
        self.node1 = node1
        self.node2 = node2
        self.distance = distance

    def connect_one_way(edge):
        edge.node1.add_edge(edge)

    def connect_bidirectional(edge):
        edge.node1.add_edge(edge)
        edge.node2.add_edge(edge)

    def _is_same(self, other):
        in_same_order = self.node1 is other.node1 and self.node2 is other.node2
        in_reverse_order = self.node1 is other.node2 and self.node2 is other.node1
        return in_same_order or in_reverse_order

    def __eq__(self, other):
        if not isinstance(other, Edge):
            return False
        return self._is_same(other)

    def __hash__(self):
        return self.n

    def __repr__(self):
        return "[{} -> {} ({})]".format(self.node1.node_id, self.node2.node_id, self.distance)
