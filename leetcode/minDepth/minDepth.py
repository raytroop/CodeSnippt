# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example:
# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
class Solution:
    def __init__(self):
        self.depths = []

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # First clear `depths`
        self.depths.clear()

        if root in [None, []]:
            return 0
        self.travPre_R(root, 1)
        print(self.depths)
        return min(self.depths)

    def travPre_R(self, node, depth):
        if node.left is None and node.right is None:
            self.depths.append(depth)
        depth += 1
        if node.left is not None:
            self.travPre_R(node.left, depth)
        if node.right is not None:
            self.travPre_R(node.right, depth)


if __name__ == '__main__':
    nodes = [TreeNode(i) for i in range(5)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[2].left = nodes[3]
    nodes[2].left = nodes[4]
    root = nodes[0]
    # print(root.val)
    # print(root.left.val)
    # print(root.right.val)
    # print(root.left.left)
    # print(root.left.right)
    solver = Solution()
    # print(solver.minDepth(root))
    # print(solver.minDepth([]))
    # print(solver.minDepth(None))
    #     0
    #    / 
    #   1  
    root = TreeNode(0)
    root.left = TreeNode(1)
    print(solver.minDepth(root))
