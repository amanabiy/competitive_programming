class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        prev = float('-inf')
        
        for i in nums:
            if prev < 0:
                prev = 0
            prev += i
            ans = max(ans, prev)

        return ans
        