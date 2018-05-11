# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        zeros = [x for x in nums if x == 0]
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        n_zeros = min(len(zeros), 3)
        res = []
        if n_zeros == 3:
            n_zeros = [0, 1]
            res.append([0,0,0])
        elif n_zeros == 2 or n_zeros == 1:
            n_zeros = [0, 1]
        else:
            n_zeros = [0]
        
        if 1 in n_zeros:
            for val_neg in neg:
                if -val_neg in pos and [val_neg, 0, -val_neg] not in res:
                    res.append([val_neg, 0, -val_neg])
        
    def sublist(self, sums, nums):
        result = []
        

        


