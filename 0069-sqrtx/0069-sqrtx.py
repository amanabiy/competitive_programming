class Solution:
    def mySqrt(self, x: int) -> int:
        """
        The sqrt of 8
        1 - 4
        
        """
        
        left = 0
        right = x
        
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return left if left * left <= x else left - 1