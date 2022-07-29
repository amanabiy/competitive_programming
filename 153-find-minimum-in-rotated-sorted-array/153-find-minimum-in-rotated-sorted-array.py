class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        if nums[0] < nums[-1] return nums[0]
        [0,1,2,3,4,5,6,7]
        [4,5,6,7,0,1,2]
         |           |
        """
        if nums[0] < nums[-1]:
            return nums[0]
        
        left = 0
        right = len(nums) - 1
        minimum = nums[0]

        while left <= right:
            mid = left + (right - left) // 2

            minimum = min(nums[mid], minimum)
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        
        return minimum
        
                    
                    
        