class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]
        extra_cables = 0
        regions = n
        
        def find(n):
            if n == parent[n]:
                return n
            parent[n] = find(parent[n])
            return parent[n]
        
        
        def union(node1, node2):
            nonlocal regions, extra_cables
            par1 = find(node1)
            par2 = find(node2)
            
            if par1 != par2:
                if rank[par1] > rank[par2]:
                    parent[par2] = par1
                    rank[par1] += rank[par2]
                else:
                    parent[par1] = par2
                    rank[par2] += rank[par1]
                regions -= 1
                
            else:
                extra_cables += 1
        
        for node_from, node_to in connections:
            union(node_from, node_to)
        # print(extra_cables, regions, math.ceil(regions / 2))

        return regions - 1 if regions - 1 <= extra_cables else -1