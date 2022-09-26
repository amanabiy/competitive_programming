class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) == 1:
            return 1

        dp = [ [0 for i in range(len(s))] for _ in range(len(s)) ]            
        
        length = 0
        while length < len(s):
            for i in range(len(dp) - 1):
                if i + length < len(s):
                    curr = i + length
                    if curr == i:
                        dp[i][curr] = 1
                    elif s[curr] == s[i]:
                        dp[i][curr] = dp[i + 1][curr - 1] + 2
                    else:
                        dp[i][curr] = max(dp[i+1][curr], dp[i][curr-1])
            length += 1
        
        return dp[0][-1]
                