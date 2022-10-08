class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        """
            0           0
        1       
            
        """
        queue = deque([(0, 'N', 0)])
        graph = defaultdict(lambda: [[], []]) # [ [red], [blue]]
        visited = set([(0, 'N')])
        ans = [-1 for i in range(n)]
        ans[0] = 0
        
        for fromN, toN in redEdges:
            graph[fromN][0].append(toN)
        
        for fromN, toN in blueEdges:
            graph[fromN][1].append(toN)
        
        while queue:

            for _ in range(len(queue)):
                node, prevColor, travel = queue.popleft()
                if node != 0:
                    if ans[node] == -1:
                        ans[node] = travel
                    else:
                        ans[node] = min(ans[node], travel)
            
                if prevColor != 'R':
                    for child in graph[node][0]:
                        if (child, 'R') not in visited:
                            queue.append((child, 'R', travel + 1))
                            visited.add((child, 'R'))
                
                if prevColor != 'B':
                    for child in graph[node][1]:
                        if (child, 'B') not in visited:
                            queue.append((child, 'B', travel + 1))
                            visited.add((child, 'B'))

        return ans
        
        
        
        
        
        