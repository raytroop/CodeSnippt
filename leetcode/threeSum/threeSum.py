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

#  !!!! Time Limit Exceeded
class Solution:
    def twoPonter(self, num1, nums, target):
        """
        :type num1: int
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        i, j = 0, len(nums) - 1
        result = []
        while i != j:
            # print(i, j)
            twoSum = nums[i] + nums[j]
            if twoSum == target:
                if [num1, nums[i], nums[j]] not in result:
                    result.append([num1, nums[i], nums[j]])
                j -= 1
            elif twoSum < target:
                i += 1
            else:
                j -= 1
        return result
        
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums = sorted(nums)

        for i in range(len(nums)-2):
            num1 = nums[i]
            res = self.twoPonter(num1, nums[i+1:], -num1)
            if res is not None:
                for pattern in res:
                    if pattern not in result:
                        result.append(pattern)
        return result

if __name__ == '__main__':
    solver = Solution()
    print(solver.threeSum([-1, 0, 1, 2, -1, -4]))

        

        


