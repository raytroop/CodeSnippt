#include <vector>
#include <iostream>
using namespace std;


class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        auto beg = nums.begin(), end = nums.end();
        auto mid = nums.begin() + (nums.end() - nums.begin())/ 2;
        while(beg != end && *mid != target){
            if (target < *mid)
                end = mid;
            else    
                beg = mid + 1;
            mid = beg + (end - beg) / 2;
        }
        return mid - nums.begin();
    }
};


int main(){
    Solution solver;
    vector<int> nums{1,3,5,6};
    cout << solver.searchInsert(nums, 5) << endl;
    cout << solver.searchInsert(nums, 2) << endl;
    cout << solver.searchInsert(nums, 7) << endl;
    cout << solver.searchInsert(nums, 0) << endl;
    return 0;
}