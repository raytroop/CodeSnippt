# Given a positive integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.

# Example:

# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

# https://leetcode.com/problems/spiral-matrix-ii/discuss/22282/4-9-lines-Python-solutions
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            A[i][j] = k + 1
            # print((i+di)%n, (j+dj)%n)
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A


if __name__ == '__main__':
    solver = Solution()
    print(solver.generateMatrix(3))





        