class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:      
        # grid = [(val, (i, j)) for v]
        n = len(grid)
        m = len(grid[0])
        minHeap = [[0, -1], [0, -1]] #[val, index]
        dp = [ [ 0 for i in range(m)] for i in range(n)]
        
        for i in range(n):
            newHeap = []
            val, firstIndex = heapq.heappop(minHeap)
            for j in range(m):
                x = grid[i][j]
                if j != firstIndex:
                    x += val
                else:
                    x += minHeap[0][0]
                dp[i][j] += x
                heapq.heappush(newHeap, [dp[i][j], j])

            minHeap = newHeap
        
        return min(dp[-1])
                                             
        