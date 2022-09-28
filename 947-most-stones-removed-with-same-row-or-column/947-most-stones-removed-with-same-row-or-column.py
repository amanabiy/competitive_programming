class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """
        """
        m, n = len(stones), len(stones[0])
        isValid = lambda r, c: 0 <= r < m and 0 <= c < n
        directions = [ (1,0), (0, 1), (-1, 0), (0, -1) ]
        cols, rows = defaultdict(list), defaultdict(list)
        ans = 0
        visited = set()
        
        def dfs(row, col):
            val = 1
            
            for r, c in rows[row]:
                if (r, c) not in visited:
                    visited.add((r, c))
                    val += dfs(r, c) 
            
            for r, c in cols[col]:
                if (r, c) not in visited:
                    visited.add((r, c))
                    val += dfs(r, c)
            
            return val
        
        
        for x, y in stones:
            cols[y].append([x, y])
            rows[x].append([x, y])
        
        for x, y in stones:
            if (x, y) not in visited:
                visited.add((x, y))
                ans += dfs(x, y) - 1
            
        return ans
        
        