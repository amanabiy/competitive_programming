class Solution:
    def integerReplacement(self, n: int) -> int:
        # count = 0
        memo = {}
        def dfs(n):
            if n == 1:
                return 0
            
            if n in memo:
                return memo[n]
            
            ans = 0
            if n % 2 == 0:
                ans = dfs(n >> 1) + 1
            else:
                adds = dfs(n + 1)
                minus = dfs(n - 1)
                ans = min(adds, minus) + 1
            memo[n] = ans
            return ans

        return dfs(n)