class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        """
            a   c   f   g   b   d
        edtdb
        """
        dp = {}
        for i in range(ord('a'), ord('z') + 1):
            dp[chr(i)] = 0 
        
        for letter in s:
            maxim = 0
            for i in range(max(ord(letter) - k, ord('a')), min(ord(letter) + k + 1, ord('z') + 1)):
                maxim = max(maxim, dp[chr(i)])
            dp[letter] = max(dp[letter], 1 + maxim)
            
        return max(dp.values())
        
        