class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """
        0: 2, 3
        1: 2
           0
         2   3
       1
        """
        graph = defaultdict(list)
        visited = set()
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(node):
            ans = 0
            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    ans += (dfs(neigh))
                    
            if ans == 0:
                return 2 if hasApple[node] else 0

            return ans + 2
        
        visited.add(0)
        ans = dfs(0)
        return ans - 2 if ans else 0