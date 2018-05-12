// https://www.cnblogs.com/x1mercy/p/7802167.html
// # Definition for a binary tree node.
// # class TreeNode(object):
// #     def __init__(self, x):
// #         self.val = x
// #         self.left = None
// #         self.right = None

// class Solution(object):
//     def isSameTree(self, p, q):
//         """
//         :type p: TreeNode
//         :type q: TreeNode
//         :rtype: bool
//         """
//         if p==None and q==None:
//             return True
//         if p==None or q==None:
//             return False
//         if p.val==q.val:
//             return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
//         return False

#include <iostream>
using namespace std;
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(p == NULL && q == NULL)
            return true;
        if(p == NULL || q == NULL)
            return false;
        if(p->val == q->val)
            return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
        return false;
        
    }
};