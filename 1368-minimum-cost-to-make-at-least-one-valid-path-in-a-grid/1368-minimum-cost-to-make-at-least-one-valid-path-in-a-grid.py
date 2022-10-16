class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        """
        [
          [3,2,2,2,1,1,3],
          [1,1,1,1,1,2,3],
          [1,1,4,1,1,1,1],
        ]
        """
        n, m = len(grid), len(grid[0])
        dp = [ [ inf for i in range(m)] for _ in range(n) ]
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        isValid = lambda r, c: 0 <= r < n and 0 <= c < m
        queue = newLevel = []
        cost = 0
        
        def dfs(i, j):
            if not (isValid(i, j) and dp[i][j] == inf): return
            dp[i][j] = cost
            newLevel.append((i, j))
            dfs(i + DIRECTIONS[grid[i][j] - 1][0], j + DIRECTIONS[grid[i][j] - 1][1])
        
        dfs(0, 0)
        queue = newLevel

        while queue:
            cost += 1
            newLevel = []
            for i, j in queue:
                for x, y in DIRECTIONS:
                    nr, nc = i + x, j + y
                    dfs(nr, nc)
            queue = newLevel
        
        return dp[-1][-1]