# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character 
# while preserving the order of characters. 
# No two characters may map to the same character but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

# Example 3:
# Input: s = "paper", t = "title"
# Output: true
# Note:
# You may assume both s and t have the same length.


class Solution:
    
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t_unique = set(t)
        for c in t_unique:
            idx_t = [i for i in range(len(s)) if t[i] == c]
            c_s = s[idx_t[0]]
            idx_s = [i for i in range(len(t)) if s[i] == c_s]
            if len(idx_t) != len(idx_s) or idx_t != idx_s:
                return False
        return True

if __name__ == '__main__':
    solver = Solution()
    print(solver.isIsomorphic(s = "egg", t = "add"))
    print(solver.isIsomorphic(s = "foo", t = "bar"))
    print(solver.isIsomorphic(s = "paper", t = "title"))


# https://leetcode.com/problems/isomorphic-strings/discuss/57941/Python-different-solutions-(dictionary-etc).
def isIsomorphic1(self, s, t):
    d1, d2 = {}, {}
    for i, val in enumerate(s):
        d1[val] = d1.get(val, []) + [i]
    for i, val in enumerate(t):
        d2[val] = d2.get(val, []) + [i]
    return sorted(d1.values()) == sorted(d2.values())

def isIsomorphic4(self, s, t): 
    return [s.find(i) for i in s] == [t.find(j) for j in t]

            
