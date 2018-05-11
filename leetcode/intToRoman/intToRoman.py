# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.

# Example 1:
# Input: 3
# Output: "III"

# Example 2:
# Input: 4
# Output: "IV"

# Example 3:
# Input: 9
# Output: "IX"

# Example 4:
# Input: 58
# Output: "LVIII"
# Explanation: C = 100, L = 50, XXX = 30 and III = 3.

# Example 5:
# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

class Solution:
    dt = {1:'I', 4:'IV', 5:'V', 9:'IX', 10: 'X', 40:'XL', 50:'L',
            90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'} 
    keys = sorted(dt.keys(), reverse=True)
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ''
        for key in self.keys:
            digit = num // key
            result += digit * self.dt[key]
            num -= key * digit
        return result
            


if __name__ == '__main__':
    dt = {1:'I', 4:'IV', 5:'V', 9:'IX', 10: 'X', 40:'XL', 50:'L',
            90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'} 
    keys = sorted(dt.keys(), reverse=True)
    print(keys)
    # print('a'+'b'*0)
    solver = Solution()
    print(solver.intToRoman(3))
    print(solver.intToRoman(4))
    print(solver.intToRoman(9))
    print(solver.intToRoman(58))
    print(solver.intToRoman(1994))
    print(solver.intToRoman(None))