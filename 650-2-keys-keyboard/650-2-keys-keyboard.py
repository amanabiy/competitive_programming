class Solution:
    def minSteps(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        dp[1] = 0
        
        for i in range(2, n // 2 + 1):
            temp = dp[i] + 2
            for j in range(i + i, n + 1, i):
                dp[j] = min(dp[j], temp)
                temp += 1

        return dp[-1]
                