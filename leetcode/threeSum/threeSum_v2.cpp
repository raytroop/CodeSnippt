#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        for (int i=0; i<int(nums.size())-2; i++){   // usigned cast to int
            if(i>0 && nums[i] == nums[i-1])
                continue;
            int l = i+1, r = nums.size() -1 ;
            while(l < r){
                int s = nums[i] + nums[l] + nums[r];
                if(s < 0)
                    ++l;
                else if(s > 0)
                    --r;
                else{
                    res.push_back(vector<int>{nums[i], nums[l], nums[r]});
                    while(l < r && nums[l] == nums[l+1])
                        ++l;
                    while(l < r && nums[r] == nums[r-1])
                        --r; 
                    ++l;
                    --r;   
                }
            }
        }
        return res;
        
    }
};


int main(){
    vector<int> vec;
    cout << vec.size() - 2 << endl; // usigned should be mixed with signed
    return 0;
}

// (tf) raytroop@myserver:~/CodeSnippt/leetcode/threeSum$ ./a.out
// 18446744073709551614