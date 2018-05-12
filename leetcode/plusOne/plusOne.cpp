#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int cn = 1;
        int size = digits.size();
        vector<int> res(size);
        int digit;
        for(int i=size-1; i>=0; --i){
            digit = digits[i];
            res[i] = (digit + cn) % 10;
            cn = (digit + cn) / 10;
        }
        if(cn)
            res.insert(res.begin(), cn);
        return res;
    }
};

int main(){
    vector<int> digits{1,2,3};
    Solution solver;
    vector<int> res = solver.plusOne(digits);
    for(auto digit: res)
        cout << digit << " ";
    cout << endl;

    digits = {9};
    res = solver.plusOne(digits);
    for(auto digit: res)
        cout << digit << " ";
    cout << endl;
}