# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

# https://www.jianshu.com/p/d3947dd9715b
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if 0==n:
            return 0
        m = len(grid[0])
        if 0==m:
            return 0
        dp = [[0]*m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if 0==i and 0==j:
                    dp[0][0] = grid[0][0]
                elif 0==i:
                    dp[0][j] = grid[0][j] + dp[0][j-1]
                elif 0==j:
                    dp[i][0] = grid[i][0] + dp[i-1][0]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

if __name__ == '__main__':
    solver = Solution()
    print(solver.minPathSum([
                            [1,3,1],
                            [1,5,1],
                            [4,2,1]
                            ]))
