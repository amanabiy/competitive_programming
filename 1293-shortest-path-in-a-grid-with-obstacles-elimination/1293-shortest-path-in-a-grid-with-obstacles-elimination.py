class Solution:
    def inBound(self, row, col, n, m):
        return 0 <= row < n and 0 <= col < m
    
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        minStep = 0
        queue = deque([(k, 0, 0)])
        n, m = len(grid), len(grid[0])
        powerReach = [ [-1] * m for _ in range(n) ]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        powerReach[0][0] = k

        while queue:
            
            for _ in range(len(queue)):
                power, row, col = queue.popleft()
                if row == n - 1 and col == m - 1:
                    return minStep

                for x, y in directions:
                    newRow = row + x
                    newCol = col + y
                    if self.inBound(newRow, newCol, n, m):
                        if grid[newRow][newCol] and power and powerReach[newRow][newCol] < power - 1:
                            powerReach[newRow][newCol] = power - 1
                            queue.append((power - 1, newRow, newCol))
                        elif not grid[newRow][newCol] and powerReach[newRow][newCol] < power:
                            powerReach[newRow][newCol] = power
                            queue.append((power, newRow, newCol))
            minStep += 1
        
        return -1
        
            
            