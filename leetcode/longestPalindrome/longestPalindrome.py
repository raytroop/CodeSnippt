# Given a string s, find the longest palindromic substring in s. 
# You may assume that the maximum length of s is 1000.

# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
# Input: "cbbd"
# Output: "bb"

# cf. https://github.com/majialin/leetcode
class Solution:
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palindromic_list = []
        for i in range(len(s)):
            lhs, rhs = i-1, i       # longest palindrome with even length
            palindromic_str = ''
            while lhs>=0 and rhs<len(s):
                if s[lhs] == s[rhs]:
                    palindromic_str = s[lhs:rhs+1]
                    lhs, rhs = lhs-1, rhs+1
                else: 
                    break
            palindromic_list.append(palindromic_str)

            lhs, rhs = i, i       # longest palindrome with odd length
            palindromic_str = ''
            while lhs>=0 and rhs<len(s):
                if s[lhs] == s[rhs]:
                    palindromic_str = s[lhs:rhs+1]
                    lhs, rhs = lhs-1, rhs+1
                else: 
                    break
            palindromic_list.append(palindromic_str)
        
        return max(palindromic_list, key=len, default='')
                

        

if __name__ == '__main__':
    solver = Solution()
    # print(solver.longestPalindrome("babad"))
    # print(solver.longestPalindrome("cbbd"))
    # print(solver.longestPalindrome("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"))
    # print(solver.longestPalindrome("abcda"))
    print(solver.longestPalindrome("a"))

                    
                
                