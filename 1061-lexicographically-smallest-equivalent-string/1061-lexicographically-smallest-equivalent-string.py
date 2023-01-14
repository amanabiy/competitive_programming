class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = defaultdict(lambda: float('inf'))
        minmum = {}

        n = len(s1)

        def find(node):
            if parent[node] == float('inf'):
                return node
            parent[node] = find(parent[node])
            return parent[node]

        for i in range(n):
            par1 = find(s1[i])
            par2 = find(s2[i])
            if par1 != par2:
                if par1 < par2:
                    parent[par2] = par1
                else:
                    parent[par1] = par2
        
        ans = [''] * len(baseStr)
        for j in range(len(baseStr)):
            ans[j] = find(baseStr[j])
        
        return ''.join(ans)