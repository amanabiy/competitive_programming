class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def dfs(i, j):
            if i == len(s) and j == len(p):
                return True
            if j >= len(p):
                return False
            ans = False
            if i < len(s) and s[i] == p[j] or p[j] == '.':
                ans = ans or dfs(i + 1, j + 1)
            if j < len(p) - 1 and p[j + 1] == '*':
                ans = ans or dfs(i, j + 2)
                if i < len(s) and (s[i] == p[j] or p[j] == '.'):
                    ans = ans or dfs(i + 1, j)
            
            return ans
        
        return dfs(0, 0)