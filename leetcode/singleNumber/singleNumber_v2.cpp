#include <vector>
using namespace std;
// XOR
// * 1^0 = 1 
// * 0^1 = 1 
// * n^n = 0 (一个数与自己亦或等于0) 
// * 0^n = n (0与其他数亦或等于那个数）
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int len = nums.size();
        int res = nums[0];
        for(int i=1; i<len; ++i){
            res = res ^ nums[i];
        }
        return res;
    }
};
