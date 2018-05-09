#include <iostream>
#include <string>
using namespace std;


class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.size();
        int num_max = 0;
        string str_max;
        string cstr;
        if(1 == n){
            return 1;
        }
        else 
        {
            for(int i=0; i< n-1; i++){
                cstr = s[i];
                for(int j=i+1; j< n; j++){
                    if(cstr.find(s[j]) > n)
                        cstr = cstr + s[j];
                    else
                        break;
                }
                if(cstr.size() > num_max){
                    num_max = cstr.size();
                    str_max = cstr;
                }
            }
        return num_max;    
        }
        
    }
};



int main(){
    Solution solver;
    cout << solver.lengthOfLongestSubstring("abcabcbb") << endl;
    cout << solver.lengthOfLongestSubstring("bbbbb") << endl;
    cout << solver.lengthOfLongestSubstring("pwwkew") << endl;
    cout << solver.lengthOfLongestSubstring("au") << endl;
    return 0;
}