class Solution:
    def isBipartite(self, AList: List[List[int]]) -> bool:
        color = {}

        graph = defaultdict(list)
        
        for i in range(len(AList)):
            for edge in AList[i]:
                graph[i].append(edge)
                graph[edge].append(i)
        
        def bfs(node):
            queue = deque([node])
            color = {node: True}
            
            while queue:
                n = queue.popleft()
                # check 
                for child in graph[n]:
                    if child in color:
                        if color[child] == color[n]:
                            return False
                    else:
                        childColor = not color[n]
                        color[child] = childColor
                        queue.append(child)
            
            return True

        
        for i in range(len(AList)):
            if i not in color:
                if not bfs(i):
                    return False
        
        return True
                    