class Solution:
    def minSteps(self, n: int) -> int:
        """
        """
        dp = [float('inf')] * (n + 1)
        dp[0] = dp[1] = 0
        
        for i in range(1, n + 1):
            j = i + i
            afterCopy = dp[i] + 1
            while j < n + 1:
                afterCopy += 1
                dp[j] = min(dp[j], afterCopy)
                j += i

        return dp[-1]