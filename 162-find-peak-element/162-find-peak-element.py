class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        [1,2,3,4]
        [4,3,2,1]
        [1,2,3,1]
        Linear fashion
        """
        
        n = len(nums)
        
        left = 0
        right = n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            
            if 0 < mid < n - 1 and nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
                return mid
            
            if mid < n- 1 and nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        return left