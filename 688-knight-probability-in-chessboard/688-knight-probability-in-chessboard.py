class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        """
        
        """
        inBound = lambda x, y: 0 <= x < n and 0 <= y < n
        DIRECTIONS = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        memo = {}
        
        def dfs(r, col, k):
            if k == 0:
                return inBound(r, col)
        
            if (r, col, k) in memo:
                return memo[(r, col, k)]
            
            ans = 0
            
            for x, y in DIRECTIONS:
                nr, nc = r + x, col + y
                if inBound(nr, nc):
                    ans += dfs(nr, nc, k - 1)
            
            ans = ans / 8
            memo[(r, col, k)] = ans

            return ans
    
        return dfs(row, column, k)
        
            