#include <vector>
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
    vector<int> res;
    void traversal(TreeNode* subNode){
        if(subNode == NULL)
            return;
        traversal(subNode->left);
        res.push_back(subNode->val);
        traversal(subNode->right);

    }
    vector<int> inorderTraversal(TreeNode* root) {
        res.clear();
        traversal(root);
        return res;
        
    }
};