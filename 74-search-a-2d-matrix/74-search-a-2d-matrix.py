class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ans = False
        
        def binarySearch(nums, target):
            left = 0
            right = len(nums) - 1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    return True
                
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return False
        
        
        for i in range(len(matrix) - 1, -1 , -1):
            if matrix[i][0] <= target:
                ans = ans or binarySearch(matrix[i], target)
        
        return ans
            