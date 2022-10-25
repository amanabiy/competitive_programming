class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [ [ 0 for _ in range(len(s) + 1) ] for _ in range(len(t))]
        
        for i in range(len(t)):
            dp[i][0] = 0
        
        for j in range(1, len(s) + 1):
            dp[0][j] = dp[0][j - 1]
            if s[j - 1] == t[0]:
                dp[0][j] += 1
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if i <= j:
                    dp[i][j] = dp[i][j - 1]
                    if s[j - 1] == t[i]:
                        dp[i][j] += dp[i - 1][j - 1]
        
        return dp[-1][-1]
                