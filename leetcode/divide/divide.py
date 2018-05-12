# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero.

# Example 1:
# Input: dividend = 10, divisor = 3
# Output: 3

# Example 2:
# Input: dividend = 7, divisor = -3
# Output: -2
# Note:

# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers within the 32-bit 
# signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, 
# assume that your function returns 2^31 − 1 when the division result overflows.

# !!!  Time Limit Exceeded
# INT_MAX = 2147483647
# INT_MIN = -2147483648
# class Solution(object):  
#     def divide(self, dividend, divisor):  
#         """ 
#         :type dividend: int 
#         :type divisor: int 
#         :rtype: int 
#         """ 
#         sign = 1 if (dividend>0 and divisor >0) or (dividend<0 and divisor<0) else -1
#         dividend = abs(dividend) 
#         divisor = abs(divisor)
#         if dividend < divisor:
#             return 0
#         quotient = 0
#         while(dividend >= divisor):
#             quotient += 1
#             dividend -= divisor
#         return min(max(INT_MIN, quotient*sign), INT_MAX) 

# https://blog.csdn.net/u014265088/article/details/52915430
INT_MAX = 2147483647
INT_MIN = -2147483648
class Solution(object):  
    def divide(self, dividend, divisor):  
        """ 
        :type dividend: int 
        :type divisor: int 
        :rtype: int 
        """  
        sign = 1 if (dividend>0 and divisor >0) or (dividend<0 and divisor<0) else -1
        dividend_a, divisor_a = abs(dividend), abs(divisor)  
        # 100 / 9 ==>  9 *  (2^3) + 9 * (2^1) + 9 * (2^0), then  
        # result = 2^3 + 2^1 + 2^0 = 11  
        result, shift = 0, 31  
        while shift >= 0:  
            if dividend_a >= (divisor_a << shift):      # divisor*2^shift
                dividend_a -= divisor_a << shift  
                result += 1 << shift  # result += 2^shift  
            shift -= 1 
        return min(max(INT_MIN, result*sign), INT_MAX)  

if __name__ == '__main__':
    solver = Solution()
    print(solver.divide(10, 3))
    print(solver.divide(7, -3))
    print(3<<2)