#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        // vector<vector<int>> res;
        // for(int k=0; k<n; ++k)
        //     res.push_back(vector<int>(n, 0));
        vector<vector<int>> res(n, vector<int> (n, 0));

        int i=0, j=0;
        int di=0, dj=1;

        for(int k=0; k<n*n; ++k){
            res[i][j] = k + 1;

            int it = (i+di)%n;
            if(it < 0)
                it = n + it;
            int jt = (j+dj)%n;
            if(jt < 0)
                jt = n + jt;
            if(res[it][jt]){
                int temp = di;
                di = dj;
                dj = -temp;
            }
            i += di;
            j += dj;
        }
        return res;    
    }
};


int main(){
    Solution solver;
    vector<vector<int>> vec = solver.generateMatrix(3);
    for(auto& x: vec){
        for(auto y: x){
            cout << y << " ";
        }
        cout << endl;
    }
    // cout << 2 % 3 << endl;
    // vector<int> vec{1,2,3};
    // cout << vec[0] << endl;
    // cout << vec[-1] << endl;
    
}