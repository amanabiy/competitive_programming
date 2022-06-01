class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        """
        Try with normal dfs
        """
        dp = grid[0].copy()
        for i in range(1, len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = min(dp[j+1:]+dp[:j]) + grid[i][j]
            dp = grid[i].copy()
        
        return min(dp)
            