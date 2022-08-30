class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        
        """
        dp = [1 for i in range(len(nums))]
        
        for i in range(len(nums)):
            old = dp[i]
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], old + dp[j])

        return max(dp)