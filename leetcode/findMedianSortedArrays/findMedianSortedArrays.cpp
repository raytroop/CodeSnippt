#include <iostream>
#include <vector>
using namespace std;


class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<double> merg;
        int sz1 = nums1.size();
        int sz2 = nums2.size();
        while(sz1 || sz2){
            if(sz1 == 0){
                merg.reserve(merg.size() + nums2.size());
                merg.insert(merg.end(), nums2.begin(), nums2.end());
                sz2 = 0;
            }
            else if(sz2 == 0){
                merg.reserve(merg.size() + nums1.size());
                merg.insert(merg.end(), nums1.begin(), nums1.end());
                sz1 = 0;
            }
            else{
                if(nums1[0] < nums2[0]){
                    merg.push_back(nums1[0]);
                    nums1.erase(nums1.begin());
                    --sz1;
                }
                else{
                    merg.push_back(nums2[0]);
                    nums2.erase(nums2.begin());
                    --sz2;
                }
            }

        }
        // for(auto x: merg)
        //     cout << x << " ";
        // cout << endl;
        int n = merg.size();
        if(n%2 != 0)
            return merg[int((n-1) / 2)];
        else
            return (merg[int(n/2)] + merg[int(n/2-1)])/2;
    }
};

int main()
{
    Solution solver;
    vector<int> nums1{1, 3};
    vector<int> nums2{2};
    cout << (solver.findMedianSortedArrays(nums1, nums2)) << endl;

    nums1 = {1, 2};
    nums2 = {3, 4};
    cout << (solver.findMedianSortedArrays(nums1, nums2)) << endl;

    nums1 = {};
    nums2 = {3, 4};
    cout << (solver.findMedianSortedArrays(nums1, nums2)) << endl;

    return 0;
}