// https://leetcode.com/problems/balanced-binary-tree/discuss/35691/The-bottom-up-O(N)-solution-would-be-better

#include <iostream>
#include <cmath>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
// 1.The first method checks whether the tree is balanced strictly 
// according to the definition of balanced binary tree: 
// the difference between the heights of the two sub trees are not bigger than 1, 
// and both the left sub tree and right sub tree are also balanced. 
class Solution {
public:
    int depth(TreeNode* subRoot){
        if(subRoot == NULL)
            return 0;
        return max(depth(subRoot->left), depth(subRoot->right)) + 1;
    }
    bool isBalanced(TreeNode* root) {
        if(root == NULL)
            return true;
        int dleft = depth(root->left);
        int dright = depth(root->right);
        return abs(dleft - dright)<=1 && isBalanced(root->left) && isBalanced(root->right);        
    }
};