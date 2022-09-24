class Solution:
    def findResult(self, graph, query):
        if query[0] not in graph or query[1] not in graph:
            return -1
        queue = deque([(query[0], 1)])
        visited = set([query[0]])
        
        while queue:
        
            for _ in range(len(queue)):
                node, value = queue.popleft()
            
                if node == query[1]:
                    return value
                
                for n, v in graph[node]:
                    if n not in visited:
                        visited.add(n)
                        queue.append((n, v * value))
            # print(queue)
        return -1

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        Time: O(equation * query)
        Space: O(n)
        """
        graph = defaultdict(list)
        ans = []

        for i in range(len(equations)):
            num, div = equations[i]
            graph[num].append((div, values[i]))
            graph[div].append((num, 1 / values[i]))
        
        for query in queries:
            ans.append(self.findResult(graph, query))
        
        return ans
                    