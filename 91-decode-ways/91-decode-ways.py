class Solution:
    def numDecodings(self, s: str) -> int:
        """
        1 11 0 6
        1 11 0 6
        """
        word = list(s)
        memo = {}
        
        def dfs(i):            
            if i == len(word):
                return 1
            if i in memo:
                return memo[i]
            ans = 0
            if word[i] != "0":
                ans += dfs(i+1)
                if i < len(word) - 1 and word[i] + word[i+1] <= "26":
                    ans += dfs(i+2)
            
            memo[i] = ans
            return ans
        
        return dfs(0)