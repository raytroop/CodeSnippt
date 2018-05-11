#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        string s = std::to_string(x);
        string temp(s);
        std::reverse(temp.begin(), temp.end());
        return temp == s;

    }
};

int main(){
    Solution solver;
    cout << solver.isPalindrome(121) << endl;
    cout << solver.isPalindrome(-121) << endl;
    cout << solver.isPalindrome(10) << endl;
    return 0;
}