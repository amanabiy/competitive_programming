class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        totalCost = 0
        visited = set()
        frontier = [[0, 0]]
        
        while len(visited) < len(points):
            distance, node = heapq.heappop(frontier)
            if node in visited:
                continue
            visited.add(node)
            totalCost += distance
            for i in range(len(points)):
                if i not in visited:
                    d = abs(points[node][0] - points[i][0]) + abs(points[node][1] - points[i][1])
                    heapq.heappush(frontier, [d, i])

        return totalCost