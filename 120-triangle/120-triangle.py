class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def dfs(row, col , memo):
            if row >= len(triangle) or col >= len(triangle[row]):
                return 0
            if (row, col) in  memo:
                return memo[(row, col)]
            memo[(row,col)] = triangle[row][col] + min(dfs(row + 1, col, memo), dfs(row+1,col+1,memo))
            return memo[(row,col)]
        return dfs(0,0,{})