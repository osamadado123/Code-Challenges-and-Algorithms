import pytest
from challenge01 import  *


def test1():
    tree1 = TreeNode(7)
    tree1.left = TreeNode(2)
    tree1.left.left = TreeNode(1)
    tree1.left.right = TreeNode(5)
    tree1.right = TreeNode(9)
    tree1.right.right = TreeNode(14)
    actual = Solution(tree1,7)
    expected = True
    assert actual == expected


def test2():
    tree1 = TreeNode(7)
    tree1.left = TreeNode(2)
    tree1.left.left = TreeNode(1)
    tree1.left.right = TreeNode(5)
    tree1.right = TreeNode(9)
    tree1.right.right = TreeNode(14)
    actual = Solution(tree1, 25)
    expected = False
    assert actual == expected

def test3():
    tree1 = TreeNode(8)
    tree1.left = TreeNode(4)
    tree1.left.left = TreeNode(2)
    tree1.left.right = TreeNode(6)
    tree1.right = TreeNode(1)
    tree1.right.right = TreeNode(16)
    actual = Solution(tree1, 5)
    expected = True
    assert actual == expected