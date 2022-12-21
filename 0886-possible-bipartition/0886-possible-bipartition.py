class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for p, dis in dislikes:
            graph[p].append(dis)
        
        def dfs(node, group={}, color=True):
            if node in group:
                return group[node] == color
            
            group[node] = color

            for n in graph[node]:
                if not dfs(n, group, not color):
                    return False

            return True
        
        for i in range(1, n+1):
            if not dfs(i, {}, True):
                return False
            
        return True