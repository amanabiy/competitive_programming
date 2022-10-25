class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        @lru_cache(None)
        def dfs(i, j):
            if i >= len(t):
                return 1
            if j >= len(s):
                return 0
            
            ans = 0
            if s[j] == t[i]:
                ans += dfs(i + 1, j + 1)
            ans += dfs(i, j + 1)
            
            return ans
        
        return dfs(0, 0)