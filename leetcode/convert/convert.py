# ZigZag Conversion

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:

# P     I    N
# A   L S  I G
# Y A   H R
# P     I

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (numRows <= 1 or numRows >= len(s)):
            return s

        str_list = [[] for i in range(numRows)]
        isdown = True
        idx = 0
        while(idx<len(s)):
            idx_end = min(len(s)-1, idx+numRows-2)
            if(isdown):
                for l, c in zip(str_list[:-1], s[idx: idx_end+1]):
                    l.append(c)
                idx = idx_end + 1
                isdown = False
                
            else:
                for l, c in zip(str_list[::-1][:-1], s[idx: idx_end+1]):
                    l.append(c)
                idx = idx_end + 1
                isdown = True
        rstr = ''
        for string in str_list:
            rstr += ''.join(string)
        return rstr


if __name__ == '__main__':
    solver = Solution()
    # print(len("PAYPALISHIRING"))
    print(solver.convert("PAYPALISHIRING", 4))
    # str_list = [[] for i in range(3)]
    # s = ['a', 'b']
    # for l, c in zip(str_list[:-1], s):
    #     print(l, c)
    #     l.append(c)
    # print(str_list)
                            