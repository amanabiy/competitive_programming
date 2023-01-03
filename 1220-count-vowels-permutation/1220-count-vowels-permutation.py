class Solution:
    def countVowelPermutation(self, n: int) -> int:
        rules = {
            "a": ["e"],
            "e": ["a", "i"],
            "i": ["a", "e", "o", "u"],
            "o": ["i", "u"],
            "u": ["a"],
        }
        mod = 10 ** 9 + 7
        dp = [{"a":0, "e":0, "i":0, "o":0, "u":0} for _ in range(n)]
        
        for key in rules:
            dp[0][key] = 1
        
        for i in range(n - 1):
            for key in rules:
                for follow in rules[key]:
                    dp[i + 1][follow] = (dp[i + 1][follow] +  dp[i][key]) % mod
        
        return sum(dp[-1].values()) % mod