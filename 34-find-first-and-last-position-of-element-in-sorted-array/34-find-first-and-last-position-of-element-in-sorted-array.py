class Solution:
    def searchRange(self, numss: List[int], target: int) -> List[int]:
        
        def binarySearch(nums, target, start):
            left = 0
            right = len(nums) - 1
            position = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    position = mid
                    
                    if start:
                        right = mid - 1
                    else:
                        left = mid + 1
                    
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return position
    
        start = binarySearch(numss, target, True)
        end = binarySearch(numss, target, False)
    

        return [start, end]