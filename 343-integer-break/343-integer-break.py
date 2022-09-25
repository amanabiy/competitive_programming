class Solution:
    def integerBreak(self, n: int) -> int:
        """
        """
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if j < n - 1:
                    dp[j] = max(dp[j], j)
                dp[j] = max(dp[j], i * dp[j - i])

        return dp[-1]