class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        left = 0
        right = len(arr) - 1
        
        while left < right:
            if arr[left] == 0:
                right -= 1
            left += 1
        
        i = len(arr) - 1
        if left == right and arr[right] == 0:
            arr[i] = 0
            right -= 1
            i -= 1

        while right >= 0:
            if arr[right] == 0:
                arr[i] = arr[right]
                i -= 1
            arr[i] = arr[right]
            i -= 1
            right -= 1
            