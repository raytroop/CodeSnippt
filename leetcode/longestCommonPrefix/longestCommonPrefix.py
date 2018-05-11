# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        rstr = ""
        strlist = list(zip(*strs))
        for prefix in strlist:
            c = list(set(prefix))
            if(len(c) == 1):
                rstr += c[0]
            else:
                break
        return rstr



if __name__ == "__main__":
    # strs = ["flower","flow","flight"]
    # strlist = list(zip(*strs))
    # print(strlist)
    solver = Solution()
    print(solver.longestCommonPrefix(["flower","flow","flight"]))
    print(solver.longestCommonPrefix(["dog","racecar","car"]))
