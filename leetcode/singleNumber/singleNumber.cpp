#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
using namespace std;

//  Example 1:
//  Input: [2,2,1]
//  Output: 1

//  Example 2:
//  Input: [4,1,2,1,2]
//  Output: 4
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        if(nums.size() == 1)
            return nums[0];
        int maxNum = *max_element(nums.cbegin(), nums.cend());
        int minNum = *min_element(nums.cbegin(), nums.cend());
        int totalNum = maxNum - minNum + 1;
        vector<int> record(totalNum);
        for(int i=0; i<int(nums.size()); ++i){
            if(record[nums[i] - minNum] == 0)
                record[nums[i] - minNum] += 1;
            else if(record[nums[i] - minNum] == 1)
                record[nums[i] - minNum] = -1;
        }
        return int(find(record.cbegin(), record.cend(), 1) - record.cbegin()) + minNum;     
    }
};




int main(){
    vector<int> vec{2,2,1};
    // int maxNum = *max_element(vec.cbegin(), vec.cend());
    // vector<int> record(maxNum);
    // cout << int(find(vec.cbegin(), vec.cend(), 1) - vec.cbegin()) << endl;
    Solution solver;
    cout << solver.singleNumber(vec) << endl;
    vec = {4,1,2,1,2};
    cout << solver.singleNumber(vec) << endl;
    vec = {-2};
    cout << solver.singleNumber(vec) << endl;
}