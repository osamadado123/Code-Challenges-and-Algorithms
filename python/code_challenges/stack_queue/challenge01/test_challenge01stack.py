# Write your test here
from challenge01stack import MyQueue


def test_queue():
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    assert q.pop() == 1
    assert q.pop() == 2
    assert q.peek() == 3
    assert q.empty() == False