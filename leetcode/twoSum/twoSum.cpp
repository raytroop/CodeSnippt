#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        for(int i=0; i<n-1; i++){
            for(int j=i+1; j<n; j++){
                int re = nums[i] + nums[j];
                if(re == target){
                    vector<int> idx{i, j};
                    return idx;
                }

            }
        }
        vector<int> idx;
        return idx;        
    }
};


int main(){
    Solution solver;
    int target=6;
    vector<int> nums{3, 2, 4};
    vector<int> idx = solver.twoSum(nums, target);
    // cout << idx[0] << idx[1] << endl;
    for(auto it = idx.cbegin(); it != idx.cend(); ++it)
        cout << *it << endl;
    return 0;
}