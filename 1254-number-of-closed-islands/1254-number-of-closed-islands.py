class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        isValid = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[r])
        count = 0
        
        def dfs(row, col):
            if not isValid(row, col):
                return False
            
            ans = True

            for x, y in directions:
                r, c = row + x, col + y                
                if isValid(r, c):
                    if grid[r][c] == 0:
                        grid[r][c] = 1
                        ans = dfs(r, c) and ans
                else:
                    ans = False
                
            return ans
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visited and grid[i][j] == 0:
                    grid[i][j] = 1
                    if dfs(i, j):
                        count += 1
        return count
        
        