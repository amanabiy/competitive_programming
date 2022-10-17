class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[mid - 1]:
                left = mid + 1
            else:
                right = mid
            # print(left, right, mid)
    
        # print("not reachable")
        return left - 1 if left > 0 else 0
                                                              
            
            