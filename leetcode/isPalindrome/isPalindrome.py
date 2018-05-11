# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:
# Input: 121
# Output: true

# Example 2:
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:

# Coud you solve it without converting the integer to a string?

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        s_reverse = s[::-1]
        issame = all(x == y for x, y in zip(s, s_reverse))
        return issame

if __name__ == '__main__':
    solver = Solution()
    print(solver.isPalindrome(121))
    print(solver.isPalindrome(-121))
    print(solver.isPalindrome(10))