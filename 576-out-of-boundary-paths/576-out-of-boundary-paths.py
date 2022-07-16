class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        isValid = lambda x, y: 0 <= x < m and 0 <= y < n
        directions = [ (0, 1), (1, 0), (-1, 0), (0, -1) ]
        memo = {}
        
        def dfs(i, j, moves):
            ans = 0
            if (i, j, moves) in memo:
                return memo[(i,j,moves)]
            
            if moves > 0:
                for x, y in directions:
                    row, col = i + x, j + y
                    if isValid(row, col):
                        ans += dfs(row, col, moves - 1)
                        
                    else:
                        ans += 1
                        
            memo[(i,j,moves)] = ans % 1000000007
            return memo[(i,j,moves)]
        
        
        
        return dfs(startRow, startColumn, maxMove)