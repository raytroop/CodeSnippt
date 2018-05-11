#include <string>
#include <vector>
#include <map>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<int> keys{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

    map<int, string> dt{{1000, "M"},{900, "CM"},{500, "D"},{400, "CD"},{100, "C"},{90, "XC"},
    {50, "L"},{40, "XL"},{10, "X"},{9, "IX"},{5, "V"},{4, "IV"},{1, "I"}};

    string intToRoman(int num) {
        string result;
        int digit;
        for(auto it=keys.begin(); it!=keys.end(); ++it){
            digit = num / (*it);
            result += repeat(dt[*it], digit);
            num -= digit * (*it);
        }
        return result;
    }

    string repeat(string s, int n){
        string temp;
        if(n==0)
            return temp;
        for(int i=0; i<n; i++)
            temp += s;
        return temp;
    }
};

// string repeat(string s, int n){
//         string temp;
//         if(n==0)
//             return temp; 
//         for(int i=0; i<n; i++)
//             temp += s;
//         return temp;
// }

int main(){
    // map<int, string> dt{{1000, "M"},{900, "CM"},{500, "D"},{400, "CD"},{100, "C"},{90, "XC"},
    // {50, "L"},{40, "XL"},{10, "X"},{9, "IX"},{5, "V"},{4, "IV"},{1, "I"}};
    // cout << dt[90] << endl;
    // cout << repeat("abc", 2) << endl;
    Solution solver;
    cout << solver.intToRoman(3) << endl;
    cout << solver.intToRoman(4) << endl;
    cout << solver.intToRoman(9) << endl;
    cout << solver.intToRoman(58) << endl;
    cout << solver.intToRoman(1994) << endl;
    return 0;
    
}