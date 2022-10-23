class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def dfs(i, j, memo):
            if i >= len(text1) or j >= len(text2):
                return 0

            if memo[i][j] != float('inf'):
                return memo[i][j]
            
            ans = 0
            if text1[i] == text2[j]:
                ans = dfs(i + 1, j + 1, memo) + 1
            else:
                takeText1 = dfs(i + 1, j, memo)
                takeText2 = dfs(i, j + 1, memo)
                ans = max(takeText1, takeText2)
            
            memo[i][j] = ans
            return ans
        
        memo = [ [ float('inf') for _ in range(len(text2)) ] for _ in range(len(text1))]
        
        return dfs(0, 0, memo)