# Example 1:
# Input: "42"
# Output: 42

# Example 2:
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign.
#              Then take as many numerical digits as possible, which gets 42.

# Example 3:
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

# Example 4:
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical 
#              digit or a +/- sign. Therefore no valid conversion could be performed.

# Example 5:
# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
#              Thefore INT_MIN (−2^31) is returned.

# INT_MAX (2^31 − 1) or INT_MIN (−2^31)

class Solution:
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        digits= [str(x) for x in range(10)]
        if len(s) == 0:
            return 0
        if len(s)==1 and s[0] in ['+', '-']:
            return 0
        if s[0] not in digits + ['+', '-']:
            return 0
        num_str = ''
        n = len(s)
        if s[0] == '+':
            sign = 1
        elif s[0] == '-':
            sign = -1
        elif s[0] in digits:
            sign = 1
            num_str = s[0] 
        
        for c in s[1:]:
            if c not in digits:
                break
            else:
                num_str += c
        
        num_str = num_str.lstrip('0')
        if len(num_str) == 0:
            return 0
        print(num_str, sign)
        if len(num_str) > len('2147483647'):
            return -2147483648 if sign < 0 else 2147483647
        elif len(num_str) < len('2147483647'):
            return sign * int(num_str)
        else:
            if sign == 1:
                for n, m in zip(num_str, '2147483647'):
                    if int(n) > int(m):
                        return 2147483647
                    elif (int(n) < int(m)):
                        return int(num_str)
                return int(num_str)    
                
            if sign == -1:
                for n, m in zip(num_str, '2147483648'):
                    if int(n) > int(m):
                        return -2147483648
                    elif (int(n) < int(m)):
                        return -int(num_str)
                return -int(num_str)


if __name__ == '__main__':
    solver = Solution()
    # print(solver.myAtoi("-91283472332"))
    # print(solver.myAtoi("+"))
    # print(solver.myAtoi("  0000000000012345678"))
    # print(solver.myAtoi("    0000000000000   "))
    print(solver.myAtoi("1095502006p8"))