class Solution:
    def minFallingPathSum(self, dp: List[List[int]]) -> int:
        for i in range(1, len(dp)):
            for j in range(len(dp[i])):
                ans = dp[i][j] + dp[i - 1][j]
                if j - 1 >= 0:
                    ans = min(ans, dp[i][j] + dp[i - 1][j - 1])
                if j + 1 < len(dp[i]):
                    ans = min(ans, dp[i][j] + dp[i - 1][j + 1])
                
                dp[i][j] = ans
        
        return min(dp[-1])