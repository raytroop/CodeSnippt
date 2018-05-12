# Given a sorted array and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:
# Input: [1,3,5,6], 5
# Output: 2

# Example 2:
# Input: [1,3,5,6], 2
# Output: 1

# Example 3:
# Input: [1,3,5,6], 7
# Output: 4

# Example 4:
# Input: [1,3,5,6], 0
# Output: 0


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        beg = 0
        end = len(nums)
        mid = beg + (end-beg) // 2
        while(beg != end and nums[mid] != target):
            if nums[mid] < target:
                beg = mid + 1
            else:
                end = mid
            mid = beg + (end - beg) // 2
        return mid


if __name__ == '__main__':
   solver = Solution()
   print(solver.searchInsert([1,3,5,6], 5))
   print(solver.searchInsert([1,3,5,6], 2))
   print(solver.searchInsert([1,3,5,6], 7))
   print(solver.searchInsert([1,3,5,6], 0))

   