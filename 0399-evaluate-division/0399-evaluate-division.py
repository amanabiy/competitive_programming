class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(lambda: [set(), {}])
        n = len(equations)
        ans = []
        
        def bfs(a, b, graph):
            if a not in graph:
                return -1

            queue = deque([(a, 1)])
            visited = set([(a, 1)])

            while queue:
                key, val = queue.popleft()

                if key == b:
                    return val

                for child in graph[key][0]:
                    if child not in visited:
                        visited.add(child)
                        queue.append((child, val * graph[key][1][child]))

            return -1

        for i in range(n):
            x, y = equations[i]
            graph[x][0].add(y)
            graph[x][1][y] = values[i]
            graph[y][0].add(x)
            graph[y][1][x] = 1 / values[i]
        
        for froQuery, toQuery in queries:
            ans.append(bfs(froQuery, toQuery, graph))  
        
        return ans