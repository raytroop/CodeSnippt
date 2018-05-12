class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        for num in nums[1:]:
            res = res ^ num
        return res

if __name__ == '__main__':
    solver = Solution()
    print(solver.singleNumber([2,2,1]))
    print(solver.singleNumber([4,1,2,1,2]))
