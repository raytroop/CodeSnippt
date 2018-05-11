#include <iostream>
#include <string>
#include <vector>
#include <limits.h>
#include <math.h>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string result;
        int n = strs.size();
        if(n==1)
            return strs[0];
        int len = INT_MAX;
        for(int i=0; i<n; ++i){
            len = min(len, int(strs[i].size()));
        }
        // cout << len << endl;
        bool commonflag;
        for(int i=0; i< len; ++i){
            commonflag = false;
            for(int j=0; j< n-1; ++j)
            {
                if(strs[j][i] == strs[j+1][i])
                    commonflag = true; 
                else{
                    commonflag = false;
                    break;
                }
            }
            // cout << commonflag << endl;
            if(commonflag)
                result += strs[0].substr(i, 1);
            else 
                return result;   
                

        }
        return result;
        
    }
};


int main(){
    // for(int i=0; i<5; ++i){
    //     int j = 100;
    //     cout << i + j << endl;
    // }
    // if(~false)
    //     cout << "TURE" << endl;
    Solution solver;
    vector<string> strs{"flower","flow","flight"};
    cout << solver.longestCommonPrefix(strs) << endl;
    strs = {"a"};
    cout << solver.longestCommonPrefix(strs) << endl;
    return 0;
}