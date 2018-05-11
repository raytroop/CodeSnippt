# Given a 32-bit `signed integer, reverse digits of an integer.

# Example 1:
# Input: 123
# Output: 321

# Example 2:
# Input: -123
# Output: -321

# Example 3:
# Input: 120
# Output: 21

# !!!!!Time Limit Exceeded
# class Solution:
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         e=1
#         temp = x
#         while True:
#             temp = temp // 10
#             if(temp):
#                 e += 1
#             else: 
#                 break
#         result = 0
#         for i in range(e):
#             mod = x % 10
#             x = x // 10
#             a = 10**(e-1-i) * mod
#             result += a
#         return result

class Solution: 
    def reverse(self, x): 
        """ 
        :type x: int 
        :rtype: int 
        """ 
        if x<0: 
            sign = -1 
        else: 
            sign = 1 
        strx=str(abs(x)) 
        r = int(strx[::-1]) 
        if r > 2147483647: 
            return 0; 
        return sign*int(r)
    def reverse_v2(self, x):
        res = 0
        if x > 2147483647: 
            return 0; 
        while x != 0:
            if(abs(res)> 2147483647 / 10):
                return 0
            res = res * 10 + x % 10
            x = x // 10
        return res
        

if __name__ == '__main__':
    solver = Solution()
    print(solver.reverse_v2(1000000009))
    # print(solver.reverse(120))
    # print(solver.reverse(1))
    # s = list(str(123))
    # print(s)
    # s = int(''.join(s[::-1]))
    # print(s)
