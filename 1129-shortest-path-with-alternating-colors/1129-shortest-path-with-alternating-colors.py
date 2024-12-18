class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        """
            0           0
        1       
            
        """
        queue = deque([(0, -1, 0)])
        graph = defaultdict(lambda: [[], []]) # [ [red], [blue]]
        visited = set([(0, -1)])
        ans = [-1 for i in range(n)]
        ans[0] = 0
        
        for fromN, toN in redEdges:
            graph[fromN][0].append(toN)
        
        for fromN, toN in blueEdges:
            graph[fromN][1].append(toN)
        
        while queue:

            for _ in range(len(queue)):
                node, prevColor, travel = queue.popleft()

                if ans[node] == -1:
                    ans[node] = travel

                a = []
                if prevColor != True:
                    a.append(True)
                if prevColor != False:
                    a.append(False)

                for x in a:
                    for child in graph[node][x]:
                        if (child, x) not in visited:
                            queue.append((child, x, travel + 1))
                            visited.add((child, x))
            
        return ans
        
        
        
        
        
        