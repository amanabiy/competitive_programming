class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def  binarySearch(arr, target, isStart = True):
            left = 0
            right = len(arr) - 1
            lastFoundIndex = -1
            
            while left <= right:
                mid = left + (right - left) // 2
    
                if arr[mid] == target:
                    lastFoundIndex = mid
                    if isStart:
                        right = mid - 1
                    else:
                        left = mid + 1
                    continue
                
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1              
                    
            return lastFoundIndex


        starts = binarySearch(nums, target, True)
        ends = binarySearch(nums, target, False)
        
        return [starts, ends]