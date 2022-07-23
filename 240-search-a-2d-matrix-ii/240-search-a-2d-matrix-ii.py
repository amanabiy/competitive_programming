class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binarySearch(arr, target):
            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = left + ((right - left) // 2)
                
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    left = mid + 1
                elif arr[mid] > target:
                    right = mid - 1
            
            return False
        
    
        i = 0
        while i < len(matrix):
            if matrix[i][0] > target:
                break
            if binarySearch(matrix[i], target):
                return True
            i += 1
        
        return False
