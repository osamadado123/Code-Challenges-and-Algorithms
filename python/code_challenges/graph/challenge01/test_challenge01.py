
from challenge01 import *
graph = Graph()


graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_edge(1, 2, 5)
graph.add_edge(1, 3, 2)
graph.add_edge(2, 3, 1)
graph.add_edge(2, 4, 3)
graph.add_edge(3, 4, 7)

def test1():
    assert graph.bft(1) == [1, 2, 3, 4]

def test2():
    assert graph.bft(2) == [2, 3, 4]

def test3():
    assert graph.bft(3) == [3, 4]

def test4():
    assert graph.bft(4) == [4]
