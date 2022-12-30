class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        cols = [0] * m
        rows = [0] * n
        diff = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]
        
        for i in range(n):
            for j in range(m):
                diff[i][j] = (cols[j] + rows[i]) * 2 - m - n
        
        return diff
    