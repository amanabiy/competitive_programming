class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        visited = set()
        height = len(grid)
        width = len(grid[0])
        memo = {}
        def dfs(row, col):
            if (row, col) in memo:
                return memo[(row, col)]
            if row >= height or col >= width:
                return -1
            if row == height - 1 and col == width - 1:
                return grid[row][col]
            right = dfs(row, col + 1)
            down = dfs(row + 1, col)
            ans = 0
            if right == -1:
                ans = down
            elif down == -1:
                ans = right
            else:
                ans = min(right, down)
            memo[(row, col)] = ans + grid[row][col]
            return memo[(row, col)]
        
        return dfs(0,0)