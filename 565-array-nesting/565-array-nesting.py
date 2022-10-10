class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        """
        """
        
        parent = [i for i in range(len(nums))]
        rank = [ 1 for i in range(len(nums)) ]
        
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        def union(n1, n2):
            par1, par2 = find(n1), find(n2)
            
            if par1 != par2:
                if parent[par1] > parent[par2]:
                    rank[par1] += rank[par2]
                    parent[par2] = par1
                else:
                    rank[par2] += rank[par1]
                    parent[par1] = par2
        
            
        for i, num in enumerate(nums):
            union(i, num)
        # print(parent)
        return max(rank)