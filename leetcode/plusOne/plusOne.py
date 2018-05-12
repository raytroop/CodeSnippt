# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

# Example 2:
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        cn = 1
        for i in range(len(digits)-1, -1, -1):
            digit = digits[i]
            digits[i] = (digit + cn) % 10
            cn = (digit + cn) // 10
        if cn:
            digits = [cn] + digits
        return digits


if __name__ == '__main__':
    solver = Solution()
    print(solver.plusOne([1,2,3]))
    print(solver.plusOne([4,3,2,1]))
    print(solver.plusOne([9]))
