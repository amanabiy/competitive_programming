class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        
        for i in range(n):
            dp[i + 1] += dp[i]
            if i < n - 1:
                dp[i + 2] += dp[i]

        return dp[-1]