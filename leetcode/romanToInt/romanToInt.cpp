#include <string>
#include <vector>
#include <map>
#include <iostream>
using namespace std;

class Solution {
public:
    map<string, int> dt{{"M", 1000},{"CM",900},{"D",500},{"CD",400},{"C",100},{"XC",90},
    {"L",50},{"XL",40},{"X",10},{"IX",9},{"V",5},{"IV",4},{"I",1}};
    int romanToInt(string s) {
        int i = 0;
        int n = s.size();
        int result=0;
        string substr;
        while(i < n-1){
            substr = s.substr(i, 2);
            if(dt[substr]){
                result += dt[substr];
                i += 2;
            }
            else{
                substr = s.substr(i, 1);
                result += dt[substr];
                i += 1;
            }

        }
        if(i == n)
            return result;
        else    
            return result + dt[s.substr(i, 1)];
        
    }
};


int main(){
    // map<string, int> dt{{"M", 1000},{"CM",900},{"D",500},{"CD",400},{"C",100},{"XC",90},
    // {"L",50},{"XL",40},{"X",10},{"IX",9},{"V",5},{"IV",4},{"I",1}};
    // if(dt["a"])
    //     cout << "inside" << endl;
    // else 
    //     cout << "outside" << endl;
    Solution solver;
    cout << solver.romanToInt("III") << endl;
    cout << solver.romanToInt("IV") << endl;
    cout << solver.romanToInt("IX") << endl;
    cout << solver.romanToInt("LVIII") << endl;
    cout << solver.romanToInt("MCMXCIV") << endl;

    return 0;
}