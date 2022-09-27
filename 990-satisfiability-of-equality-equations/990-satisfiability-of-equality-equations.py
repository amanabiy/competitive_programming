class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        """
        a == b -> a: b b: a
        c == a -> a: b c: 
        
        """
        parent = {}
        rank = {}
        
        def find(node):
            # print(f"find: {node}")
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        def union(x, y):
            par1 = find(x)
            par2 = find(y)
            if par1 != par2:
                if rank[par1] > rank[par2]:
                    parent[par2] = par1
                    rank[par1] += rank[par2]
                else:
                    parent[par1] = par2
                    rank[par2] += rank[par1]
        
        
        for equation in equations:
            x, sign, y = equation[0], equation[1:3], equation[3]
            if sign == "==":
                parent[x] = x
                parent[y] = y
                rank[x] = 1
                rank[y] = 1

        for equation in equations:
            x, sign, y = equation[0], equation[1:3], equation[3]
            if sign == "==":
                union(x, y)

        for equation in equations:
            x, sign, y = equation[0], equation[1:3], equation[3]
            if sign == '!='  and (x == y or (x in parent and y in parent and find(x) == find(y))):
                return False
        
        return True