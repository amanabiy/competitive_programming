class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ans = float('-inf')
        heap = [[grid[0][0], 0, 0]]
        n = len(grid)
        m = len(grid[0])
        visited = set([(0, 0)])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        while heap:
            val, x, y = heapq.heappop(heap)
            ans = max(ans, val)
            if x == n - 1 and y == m - 1:
                return max(ans, val)
            
            for r, c in directions:
                row = x + r
                col = y + c
                if not (0 <= row < n and 0 <= col < m):
                    continue
                if (row, col) in visited:
                    continue
                visited.add((row, col))
                heapq.heappush(heap, (grid[row][col], row, col))
        
        return -1
            
        