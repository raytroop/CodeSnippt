
#include <iostream>
#include <vector>
#include <algorithm>
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
    vector<int> depths;

    void travPre_R(TreeNode* node, int depth){
        if(node->left == NULL && node->right == NULL)
            depths.push_back(depth);
        depth += 1;
        if(node->left != NULL)
            travPre_R(node->left, depth);
        if(node->right != NULL)
            travPre_R(node->right, depth);
    }
    int minDepth(TreeNode* root) {
        depths.clear();
        if(root == NULL) 
            return 0;
        travPre_R(root, 1);
        return *min_element(depths.cbegin(), depths.cend());
    }
};


int main(){
    vector<int> vec{1,2,3,-1,-2,-3};
    cout << *min_element(vec.cbegin(), vec.cend()) << endl;
    cout << *max_element(vec.cbegin(), vec.cend()) << endl;
    return 0;
}