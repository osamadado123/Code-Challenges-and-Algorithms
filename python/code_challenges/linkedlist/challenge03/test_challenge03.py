from challenge03 import Node,LinkedList
def test_del_2nd_node_from_last():
    llist = LinkedList()
    llist.append(5)
    llist.append(4)
    llist.append(3)
    llist.append(2)
    llist.append(1)

    llist.deleteNode(2)

    actual =llist.printList()
    expected = [1, 2, 3 ,5]
    assert actual == expected

def test_del_node():
    llist = LinkedList()
    llist.append(1)

    llist.deleteNode(1)

    actual =llist.printList()
    expected = []
    assert actual == expected

def test_del_one_node():
    llist = LinkedList()
    llist.append(2)
    llist.append(1)


    llist.deleteNode(1)

    actual =llist.printList()
    expected = [1]
    assert actual == expected
