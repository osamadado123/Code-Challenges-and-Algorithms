# Write your test here
from challenge01 import Node,LinkedList



def test_del_5():
    llist = LinkedList()
    node1 =llist.append(9)
    node2 =llist.append(1)
    node3 =llist.append(5)
    node4 =llist.append(4)

    llist.deleteNode(node3)
    actual = llist.__str__()

    expected = '{4}{1}{9}'
    assert actual == expected

def test_del_1():
    llist = LinkedList()
    node1 =llist.append(9)
    node2 =llist.append(1)
    node3 =llist.append(5)
    node4 =llist.append(4)

    llist.deleteNode(node2)
    actual = llist.__str__()

    expected = '{4}{5}{9}'
    assert actual == expected

