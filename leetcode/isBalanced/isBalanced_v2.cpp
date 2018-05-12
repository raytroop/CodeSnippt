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

// 2.The second method is based on DFS. Instead of calling depth() explicitly for each child node, 
// we return the height of the current node in DFS recursion. 
// When the sub tree of the current node (inclusive) is balanced, 
// the function dfsHeight() returns a non-negative value as the height. 
// Otherwise -1 is returned. According to the leftHeight and rightHeight of the two children, 
// the parent node could check if the sub tree is balanced, and decides its return value.
class solution {
public:
    int dfsHeight (TreeNode *root) {
        if (root == NULL) 
            return 0;
        
        int leftHeight = dfsHeight (root -> left);
        if (leftHeight == -1) 
            return -1;

        int rightHeight = dfsHeight (root -> right);
        if (rightHeight == -1) 
            return -1;
        
        if (abs(leftHeight - rightHeight) > 1)  
            return -1;
            
        return max (leftHeight, rightHeight) + 1;
    }
    bool isBalanced(TreeNode *root) {
        return dfsHeight (root) != -1;
    }
};