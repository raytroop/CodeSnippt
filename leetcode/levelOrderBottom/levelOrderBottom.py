# Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
# (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.vals_dict = {}
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.vals_dict.clear()
        if root in [None, []]:
            return []
        self.travPre_R(root, 1)
        num = max(self.vals_dict.keys())
        # print(self.vals_dict)
        return [self.vals_dict[num-l] for l in range(num)]

    def travPre_R(self, node, depth):
        if depth in self.vals_dict:
            self.vals_dict[depth].append(node.val)
        else:
            self.vals_dict[depth] = [node.val]

        if node.left is None and node.right is None:
            return 
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
    nodes[2].right = nodes[4]
    root = nodes[0]
    solver = Solution()
    print(solver.levelOrderBottom(root))