import pytest 
from challenge02 import Node , linkedlist
def odd_function():
    linkedList1 = linkedlist()
    node1 = Node("1")
    linkedList1.append(node1)

    node2 = Node("2")
    linkedList1.append(node2)

    node3 = Node("3")
    linkedList1.append(node3)

    node4 = Node("4")
    linkedList1.append(node4)

    node5 = Node("5")
    linkedList1.append(node5)

    return linkedList1

def even_function():
    linkedList1 = linkedlist()
    node1 = Node("1")
    linkedList1.append(node1)

    node2 = Node("2")
    linkedList1.append(node2)

    node3 = Node("3")
    linkedList1.append(node3)

    node4 = Node("4")
    linkedList1.append(node4)

    return linkedList1
def test1():
    
    one=linkedlist()
    node_one=Node("1")
    one.append(node_one)
    actual=one.find_middle()
    expected="1"
    assert actual==expected

def test_odd_nodes():
    run=odd_function()
    
    actual=run.find_middle()
    expected="3"
    assert actual==expected

def test_even_nodes():
    run=even_function()
    
    actual=run.find_middle()
    expected="3"
    assert actual==expected