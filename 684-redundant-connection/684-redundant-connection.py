class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        1: 2, 5, 4
        2: 3
        3: 4
        """
        parent = [i for i in range(len(edges))]
        
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        for froms, dest in edges:
            par1 = find(froms - 1)
            par2 = find(dest - 1)
            if par1 == par2:
                return [froms, dest]
            parent[par1] = par2
        
        return []