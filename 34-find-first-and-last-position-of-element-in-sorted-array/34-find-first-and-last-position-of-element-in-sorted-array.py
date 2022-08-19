class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def LeftOrRightMost(nums, target, leftMost = True):
            left = 0
            right = len(nums) - 1
            index = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    index = mid
                    if leftMost:
                        right = mid - 1
                    else:
                        left = mid + 1
                
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return index
        
        return [LeftOrRightMost(nums, target), LeftOrRightMost(nums, target, False)]