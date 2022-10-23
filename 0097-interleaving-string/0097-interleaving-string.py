class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
    
        s1Len = len(s1)
        s2Len = len(s2)
        dp = [ [ False for _ in range(s2Len + 1) ] for _ in range(s1Len + 1)]
        
        dp[0][0] = True

        for row in range(1, s1Len + 1):
            dp[row][0] = s1[row - 1] == s3[row - 1] and dp[row - 1][0]
        
        
        for col in range(1, s2Len + 1):
            dp[0][col] = s2[col - 1] == s3[col - 1] and dp[0][col - 1]
        
        
        for row in range(1, len(dp)):
            for col in range(1, len(dp[row])):
                if s1[row - 1] == s3[row + col - 1]:
                    dp[row][col] = dp[row - 1][col]
                if s2[col - 1] == s3[row + col - 1]:
                    dp[row][col] = dp[row][col] or dp[row][col - 1]
        
        return dp[-1][-1]
        