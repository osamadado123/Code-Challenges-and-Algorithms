class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def Solution(TreeNode, k):
    Stack, HashTable = [TreeNode], set()
    while Stack:
        node = Stack.pop()
        if k - node.val in HashTable: 
            return True
        HashTable.add(node.val)
        if node.left: 
            Stack.append(node.left)
        if node.right: 
            Stack.append(node.right)
            
    return False