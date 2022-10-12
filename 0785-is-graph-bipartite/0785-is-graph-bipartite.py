class Solution:
    def isBipartite(self, AList: List[List[int]]) -> bool:
        visited = set()

        graph = defaultdict(list)
        
        for i in range(len(AList)):
            for edge in AList[i]:
                graph[i].append(edge)
                graph[edge].append(i)
        
        def bfs(node):
            visited.add(node)
            queue = deque([node])
            setA = set([node])
            setB = set()
            while queue:
                n = queue.popleft()
                # check 
                for child in graph[n]:
                    if child in visited:
                        if n in setA and child in setA:
                            return False
                        if n in setB and child in setB:
                            return False
                    else:
                        if n in setA:
                            setB.add(child)
                        else:
                            setA.add(child)
                        visited.add(child)
                        queue.append(child)
            
            return True

        
        for i in range(len(AList)):
            if i not in visited:
                if not bfs(i):
                    return False
        
        return True
                    