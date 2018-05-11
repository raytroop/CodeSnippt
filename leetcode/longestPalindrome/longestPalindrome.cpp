#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        string palindromic_longest;
        int n = s.size();
        int lhs, rhs;
        string palindromic_str;
        for(int i=0; i<n; ++i){
            lhs = i-1;
            rhs = i;
            palindromic_str ="";
            while(lhs >=0 && rhs < n){
                if(s[lhs] == s[rhs]){
                    palindromic_str = s.substr(lhs, rhs-lhs+1);
                    lhs -= 1;
                    rhs += 1;
                }
                else
                    break;
            }
            palindromic_longest = palindromic_str.size() > palindromic_longest.size() ? palindromic_str: 
                                                    palindromic_longest;
            
            lhs=rhs=i;
            palindromic_str ="";
            while(lhs >=0 && rhs < n){
                if(s[lhs] == s[rhs]){
                    palindromic_str = s.substr(lhs, rhs-lhs+1);
                    lhs -= 1;
                    rhs += 1;
                }
                else
                    break;
            }
            palindromic_longest = palindromic_str.size() > palindromic_longest.size() ? palindromic_str: 
                                                    palindromic_longest;

            }
        return palindromic_longest;
        }   
};


int main(){
    Solution solver;
    string t("babad");
    cout << solver.longestPalindrome(t) << endl;

    t= "cbbd";
    cout << solver.longestPalindrome(t) << endl;

    t= "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa";
    cout << solver.longestPalindrome(t) << endl;
}