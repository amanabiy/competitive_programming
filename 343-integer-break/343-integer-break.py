class Solution:
    def integerBreak(self, n: int) -> int:
        """
        """
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for i in range(1, n + 1):
            for j in range(i):
                if i < n:
                    dp[i] = max(i, dp[i])
                dp[i] = max(dp[i], dp[j] * dp[i - j] )
                # dp[j] = max(dp[j], i * dp[j - i])
        # print(dp)
        return dp[-1]