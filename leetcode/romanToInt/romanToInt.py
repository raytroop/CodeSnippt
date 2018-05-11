class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dt = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50,
            'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000} 
        n = len(s)
        i = 0
        result = 0
        while(i < n-1):
            if s[i:i+2] in dt:
                result += dt[s[i:i+2]]
                i += 2
            else:
                result += dt[s[i]]
                i += 1
        if i == n:
            return result
        else:
            return result+dt[s[i]]


if __name__ == '__main__':
    solver = Solution()
    print(solver.romanToInt('III'))
    print(solver.romanToInt('IV'))
    print(solver.romanToInt('IX'))
    print(solver.romanToInt('LVIII'))
    print(solver.romanToInt('MCMXCIV'))