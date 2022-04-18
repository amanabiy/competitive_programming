class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parents = [i for i in range(len(isConnected))]
        self.count = len(isConnected)
        rank = [1] * len(isConnected)
        def find(node):
            if parents[node] == node:
                return node
            parents[node] = find(parents[node])
            return parents[node]
        
        def union(node1,node2):
            par1 = find(node1)
            par2 = find(node2)
            
            if par1 != par2:
                self.count -= 1
                if rank[par1] > rank[par2]:
                    parents[par2] = par1
                elif rank[par2] > rank[par1]:
                    parents[par1] = par2
                else:
                    parents[par2] = par1
                    rank[par1] += 1
    
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j]:
                    union(i,j)
        
        
        return self.count
                
                
        
        
            
                    
            
            
        
        
                  