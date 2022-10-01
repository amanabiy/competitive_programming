class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        dp = [ 0 for _ in range(len(s)+1) ]
    
        dp[0] = 1
        
        for i in range(len(s)):
            if s[i] != '0':
                dp[i + 1] += dp[i]
            if i - 1 >= 0 and s[i-1] != '0' and int(s[i - 1] + s[i]) <= 26:
                dp[i + 1] += dp[i - 1]
            
        return dp[-1]
            
                                                                