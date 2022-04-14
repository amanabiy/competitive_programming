class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outdegree = {i:0 for i in range(len(graph))}
        graphs = defaultdict(list)
        queue = deque()
        ans = []
        
        for i, edge in enumerate(graph):
            for k in edge:
                graphs[k].append(i)
            outdegree[i] = len(graph[i])
            
        for key in outdegree.keys():
            if outdegree[key] == 0:
                queue.append(key)
        
        while queue:
            node = queue.popleft()
            ans.append(node)
            for neigh in graphs[node]:
                outdegree[neigh] -= 1
                if outdegree[neigh] == 0:
                    queue.append(neigh)
    
        return sorted(ans)