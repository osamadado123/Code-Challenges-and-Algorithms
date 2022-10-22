# Write your test here
from challenge01 import Node,LinkedList



def test_del_5():
    llist = LinkedList()
    llist.append(9)
    llist.append(1)
    llist.append(5)
    llist.append(4)

    llist.deleteNode(5)
    actual = llist.printList()

    expected = [4,1,9]
    assert actual == expected

def test_del_1():
    llist = LinkedList()
    llist.append(9)
    llist.append(1)
    llist.append(5)
    llist.append(4)

    llist.deleteNode(1)
    actual = llist.printList()

    expected = [4,5,9]
    assert actual == expected

def test_del_9():
    llist = LinkedList()
    llist.append(9)
    llist.append(1)
    llist.append(5)
    llist.append(4)

    llist.deleteNode(9)
    actual = llist.printList()

    expected = [4,5,1]
    assert actual == expected