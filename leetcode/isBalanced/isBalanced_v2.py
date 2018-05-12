# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfsHeight(self, subRoot):
        if subRoot is None:
            return 0
        lheight = self.dfsHeight(subRoot.left)
        if lheight == -1:
            return -1
        rheight = self.dfsHeight(subRoot.right)
        if rheight == -1:
            return -1
        if abs(lheight - rheight) > 1:
            return -1
        return max(lheight, rheight) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfsHeight(root) != -1