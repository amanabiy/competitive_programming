class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        [1,2,3,4]
        [4,3,2,1]
        [1,2,3,1]
        Linear fashion
        """
        
        n = len(nums)
        
        if len(nums) >= 2 and nums[0] > nums[1]:
            return 0
        
        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                return i
        
        return n - 1