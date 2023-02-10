class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        [1,2,3,4,5,6,7]
        [1,3,5,7]
        [2,4,6]
        """
        nums = nums1 + nums2
        nums.sort()
        middle = len(nums) // 2
        if len(nums) % 2 == 0:
            return (nums[middle] + nums[middle - 1]) / 2
        return nums[middle]