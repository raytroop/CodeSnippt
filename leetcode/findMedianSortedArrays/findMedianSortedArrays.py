# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0


# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merg = list()
        while(nums1 or nums2):
            if len(nums1)==0 :
                merg = merg + nums2
                nums2 = []
            elif len(nums2)==0 :
                merg = merg + nums1
                nums1 = []
            else:
                if(nums1[0] < nums2[0]):
                    merg.append(nums1[0])
                    nums1 = nums1[1:] if len(nums1) > 1 else []
                else:
                    merg.append(nums2[0])
                    nums2 = nums2[1:] if len(nums2) > 1 else []
        n = len(merg)
        if(n%2 != 0):
            return merg[int((n-1) / 2)]
        else:
            return (merg[int(n/2)] + merg[int(n/2-1)])/2

if __name__ == '__main__':
    solver = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    print(solver.findMedianSortedArrays(nums1, nums2))

    nums1 = [1, 2]
    nums2 = [3, 4]
    print(solver.findMedianSortedArrays(nums1, nums2))

    nums1 = []
    nums2 = [3, 4]
    print(solver.findMedianSortedArrays(nums1, nums2))
