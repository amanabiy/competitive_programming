class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        find the column,find the row
        """
#         def binarySearch(find, arr):
#             mid = len(arr) // 2
#             left = 0
#             right = len(arr) - 1
    
#             while left <= right:
#                 mid = (left + right) // 2
#                 if arr[mid] 
        
        # find the column
        vindex = 0
        
        while vindex < len(matrix) and matrix[vindex][0] <= target:
            if matrix[vindex][0] == target:
                return True
            vindex += 1
        
        vindex -= 1
        left = 0
        right = len(matrix[vindex]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            # print(left, right, mid)
            if matrix[vindex][mid] == target:
                return True
            elif matrix[vindex][mid] < target:
                left = mid + 1
            elif matrix[vindex][mid] > target:
                right = mid - 1
                
        return False
        