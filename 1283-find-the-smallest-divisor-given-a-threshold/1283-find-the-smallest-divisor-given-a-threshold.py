class Solution:
    def divSum(self, divisor, nums):
        total_sum = 0
        for num in nums:
            total_sum += math.ceil(num / divisor)
        return total_sum

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        """
        nums, thershold
        [2,2,2] threshold = 6
        one -> 
        divide every element
        find the smallest divider
        nums = [44,22,33,11,1]
         divider -> 1 - 44
         sum -> the first element -> I can be sure that the first element is the min I could find
         m -> is the maximum value in my nums 10 ** 6
         n -> the length of the nums         5 * 10 ** 4
         Time: O(n + (m * n)) -> (m * n) -> 
         
        N N N N Y Y Y Y Y Y
              r
                l     
        """
        left = 0
        right = 10 ** 6
        ans = -1
        while left <= right:
            mid = left + (right - left) // 2
            if mid != 0 and self.divSum(mid, nums) <= threshold:                
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
        