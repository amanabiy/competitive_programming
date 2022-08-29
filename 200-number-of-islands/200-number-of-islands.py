class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        """
        isValid = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[r])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ans = 0
        
        def bfs(i, j):
            queue = deque([(i, j)])
            grid[i][j] = "0"
            while queue:
                row, col = queue.popleft()
                for x, y in directions:
                    newRow, newCol = row + x, col + y
                    if isValid(newRow, newCol) and grid[newRow][newCol] == "1":
                        queue.append((newRow, newCol))
                        grid[newRow][newCol] = "0"
                        
        
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    bfs(i, j)
                    ans += 1
        
        return ans