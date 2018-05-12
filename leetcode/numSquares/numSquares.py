# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) 
# which sum to n.

# Example 1:
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.

# Example 2:
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

# https://leetcode.com/problems/perfect-squares/discuss/71475/Short-Python-solution-using-BFS
# Short Python solution using BFS
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append( i * i )
            i += 1
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x-y)
            toCheck = temp

        return cnt

if __name__ == '__main__':
    solver = Solution()
    print(solver.numSquares(4))
    print(solver.numSquares(12))
    print(solver.numSquares(13))