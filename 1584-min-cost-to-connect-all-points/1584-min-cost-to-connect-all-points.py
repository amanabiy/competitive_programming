class Solution:
    def find(self, node, parent):
        if parent[node] == -1:
            return node
        parent[node] = self.find(parent[node], parent)
        return parent[node]

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        allConnection = []
        totalCost = 0
        parents = defaultdict(lambda: -1)
        rank = defaultdict(lambda: 1)

        # consider connecting every point to eachother
        for i, (x1, y1) in enumerate(points):
            for j in range(i + 1, len(points)):
                # calculate the distance between each point
                distance = abs(x1 - points[j][0]) + abs(y1 - points[j][1]) 
                allConnection.append([distance, (x1, y1), tuple(points[j])])
        
        allConnection.sort()
        
        for cost, point1, point2 in allConnection:
            par1 = self.find(point1, parents)
            par2 = self.find(point2, parents)
            
            if par1 != par2:
                totalCost += cost
                parents[par1] = par2
        
        return totalCost