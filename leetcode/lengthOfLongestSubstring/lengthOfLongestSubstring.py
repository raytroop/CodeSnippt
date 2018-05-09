# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        num_max = 0
        str_max = ''
        if n == 1:
            str_max = s
        else:
            for i in range(n-1):
                cstr = s[i:i+1]
                for j in range(i+1, n):
                    if s[j] not in cstr:
                        cstr = s[i:j+1]
                    else:
                        break
                if len(cstr) > num_max:
                    num_max = len(cstr)
                    str_max = cstr
        
        return str_max

if __name__ == '__main__':
    solver = Solution()
    t1 = "abcabcbb"
    t2 = "bbbbb"
    t3 = "pwwkew"
    print(solver.lengthOfLongestSubstring(t1))
    print(solver.lengthOfLongestSubstring(t2))
    print(solver.lengthOfLongestSubstring(t3))
    print(solver.lengthOfLongestSubstring('au'))
                    
