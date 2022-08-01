class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [ [0 for i in range(n)] for _ in range(m) ]
        grid[0][0] = 1
        isValid = lambda x, y: 0 <= x < m and 0 <= y < n
        
        for i in range(m):
            for j in range(n):
                if isValid(i-1, j):
                    grid[i][j] += grid[i - 1][j]
                if isValid(i, j - 1):
                    grid[i][j] += grid[i][j - 1]
                # grid[i][j] %= (2 * (10 ** 9)) 
        return grid[-1][-1] 