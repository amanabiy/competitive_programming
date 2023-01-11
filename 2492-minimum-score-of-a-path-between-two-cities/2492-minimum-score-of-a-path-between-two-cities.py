class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        memo = {}
        graph = defaultdict(list)
        parent = [i for i in range(n)]
        rank = [1] * n
        minRoad = [float('inf')] * n
        
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(city1, city2, distance):
            par1 = find(city1)
            par2 = find(city2)
            
            mnss = min([minRoad[par1], minRoad[par2], distance])
            if par1 != par2:
                # union them and consider the min distance
                if rank[par1] > rank[par2]:
                    parent[par2] = par1
                    rank[par1] += rank[par2]
                else:
                    parent[par1] = par2
                    rank[par2] += rank[par1]
            minRoad[par2] = mnss            
            minRoad[par1] = mnss
        
        
        for x, y, dist in roads:
            x -= 1
            y -= 1
            union(x, y, dist)
            
        return minRoad[find(0)]