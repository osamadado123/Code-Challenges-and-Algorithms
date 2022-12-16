from collections import deque

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        if from_node not in self.edges:
            self.edges[from_node] = [to_node]
        else:
            self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

    def bft(self, start_node):
        visited = []
        queue = deque([start_node])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
                neighbors = self.edges.get(node, [])
                for neighbor in neighbors:
                    queue.append(neighbor)
        return visited
