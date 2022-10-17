class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        left = 0
        right = len(nums)
        # nums = [float('-inf')] + nums + [float('-inf')]
        while left < right:
            mid = left + (right - left) // 2
            
            if (mid - 1 < 0 and nums[mid + 1] < nums[mid]) or (len(nums) == mid + 1 and nums[mid - 1] < nums[mid]):
                return mid
            # print(mid, left, right)
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            
            if nums[mid] > nums[mid - 1]:
                left = mid + 1
            else:
                right = mid
    
        print("not reachable")
        return left
                                                              
            
            