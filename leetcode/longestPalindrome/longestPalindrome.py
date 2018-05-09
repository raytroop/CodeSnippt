# Given a string s, find the longest palindromic substring in s. 
# You may assume that the maximum length of s is 1000.

# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
# Input: "cbbd"
# Output: "bb"


class Solution:
    def issym(self, s):
        """
        :type s: list
        :rtype: bool
        """
        n = len(s)
        lmt = n // 2 -1 
        t = [s[i] == s[-i-1] for i in range(lmt+1)]
        return all(t)
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        rstr = s[0]
        if n<2:
            rstr = s
        else:
            for i in range(n-1):
                t = [idx  for idx in range(i+1, n) if s[i]==s[idx]]
                if not t:
                    continue
                else:
                    for idx in t:
                        cstr = s[i:idx+1] if self.issym(s[i:idx+1]) else []
                        if len(cstr) > len(rstr):
                            rstr = cstr

        return rstr

if __name__ == '__main__':
    solver = Solution()
    print(solver.longestPalindrome("babad"))
    print(solver.longestPalindrome("cbbd"))
    print(solver.longestPalindrome("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"))
    print(solver.longestPalindrome("abcda"))

                    
                
                