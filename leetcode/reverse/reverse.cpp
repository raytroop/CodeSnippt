#include <iostream>
#include <limits.h>
using namespace std;

// https://www.cnblogs.com/grandyang/p/4125588.html
class Solution {
public:
    int reverse(int x) {
        int res = 0;
        while (x != 0) {
            if (abs(res) > INT_MAX / 10) return 0;
            res = res * 10 + x % 10;
            x /= 10;
        }
        return res;
    }
};


int main(){
    int x = 123;
    // int sign = x > 0 ? 1 : -1;
    // cout << sign << endl;
    // string s = to_string(x);
    // cout << s << endl;
    // reverse(s.begin(),s.end());
    // cout << s << endl;
    // cout << stoi(s) << endl;
    Solution solver;
    cout << solver.reverse(123) << endl;
    return 0;
}