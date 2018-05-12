#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int n = grid.size();
        if(0==n)
            return 0;
        int m = grid[0].size();
        if(0==m)
            return 0;
        vector<vector<int>> dp(n, vector<int>(m));
        for(int i=0; i<n; ++i){
            for(int j=0; j<m; ++j){
                if(0==i && 0==j)
                    dp[0][0] = grid[0][0];
                else if(0==i)
                    dp[0][j] = grid[0][j] + dp[0][j-1];
                else if(0==j)
                    dp[i][0] = grid[i][0] + dp[i-1][0];
                else
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]);
            }
        }
        return dp[n-1][m-1];
    }
};