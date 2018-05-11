// https://www.jianshu.com/p/b5a5697a3812
#include <string>
#include <vector>
#include <iostream>
using namespace std;


class Solution {
public:
    string convert(string s, int numRows) {
        int n = static_cast<int>(s.size());
        if(numRows <=1 || numRows>=n)
            return s;
        vector<string> rowString(numRows);
        int rowNum = 1;
        int flag = 1;
        for(int i=0; i<n; ++i){
            rowString[rowNum-1] += s[i];
            if(rowNum==1)
                flag = 1;
            if(rowNum==numRows)
                flag = -1;
            rowNum += flag;
        }
        string result;
        for(int i=0; i<numRows; ++i)
            result += rowString[i];
        return result;
    }
};


int main(){
    Solution solver;
    cout << solver.convert("PAYPALISHIRING", 4) << endl;
    return 0;
}