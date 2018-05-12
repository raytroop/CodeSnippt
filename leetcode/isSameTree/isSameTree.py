# Given two binary trees, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical and 
# the nodes have the same value.

# Example 1:
# Input:     1         1
#           / \       / \
#          2   3     2   3

#         [1,2,3],   [1,2,3]

# Output: true

# Example 2:
# Input:     1         1
#           /           \
#          2             2

#         [1,2],     [1,null,2]

# Output: false

# Example 3:
# Input:     1         1
#           / \       / \
#          2   1     1   2

#         [1,2,1],   [1,1,2]

# Output: false


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.p_vals = []
        self.q_vals = []

    def travPre_R(self, node, vals):
        vals.append(node.val)
        if node.left is None and node.right is None:
            return 

        if node.left is not None:
            self.travPre_R(node.left, vals)
        else:
            vals.append(None)

        if node.right is not None:
            self.travPre_R(node.right, vals)
        else:
            vals.append(None) 

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True    
        if p is None or q is None:
            return False
        self.p_vals.clear()
        self.q_vals.clear()
        self.travPre_R(p, self.p_vals)
        self.travPre_R(q, self.q_vals)
        # print(self.p_vals)
        # print(self.q_vals)
        if self.p_vals == self.q_vals:
            return True
        else:
            return False


if __name__ == '__main__':
    solver = Solution()

    node1a = TreeNode(1)
    node2a = TreeNode(2)
    node3a = TreeNode(1)
    node1a.left = node2a
    node2a.right = node3a
    root1 = node1a

    node1b = TreeNode(1)
    node2b = TreeNode(1)
    node3b = TreeNode(2)
    node1b.left = node2b
    node2b.right = node3b
    root2 = node1b


    print(solver.isSameTree(root1, root2))
    print(solver.isSameTree([], []))

