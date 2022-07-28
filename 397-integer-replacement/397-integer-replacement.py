class Solution:
    def integerReplacement(self, n: int) -> int:
        # count = 0
        
        def dfs(n):
            if n == 1:
                return 0

            if n % 2 == 0:
                return dfs(n//2) + 1
            else:
                adds = dfs(n+1)
                minus = dfs(n-1)
                return min(adds, minus) + 1
        
        return dfs(n)