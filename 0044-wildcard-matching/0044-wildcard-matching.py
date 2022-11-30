class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @lru_cache(None)
        def dfs(i, j):
            if j == len(p) and i == len(s):
                return True
            if j == len(p):
                return False
            
            ans = False
            if i < len(s) and s[i] == p[j] or p[j] == '?':
                ans = ans or dfs(i + 1, j + 1)
            elif p[j] == '*':
                if i < len(s):
                    ans = ans or dfs(i + 1, j) or dfs(i + 1, j + 1)
                ans = ans or dfs(i, j + 1)
    
            return ans
        
        return dfs(0, 0)
                
                