class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0 for i in range(target+1)]
        dp[0] = 1
        for i in range(target):
            for n in nums:
                if n + i <= target: dp[i+n] += dp[i]
        
        return dp[-1]