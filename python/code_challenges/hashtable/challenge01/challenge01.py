class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
data = []

def findTarget(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: bool
    """
    global data
    data = []
    if root is None:
        return False
    helper(root)
    left = 0 
    right = len(data) - 1
    temp = data[left] + data[right]
    while left < right:
        if temp == k:
            return True
        elif temp < k:
            left += 1
        else:
            right -= 1
        temp = data[left] + data[right]
    return False
    
def helper(root):
    global data
    if root.left is not None:
        helper(root.left)
    data.append(root.val)
    if root.right is not None:
        helper(root.right)
