class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        
        """
        queue = deque([[[0], 0]])
        ans = []
        
        while queue:
            path, node = queue.popleft()

            if node == len(graph) - 1:
                ans.append(path[::])
                continue
            
            for neigh in graph[node]:
                queue.append([path + [neigh], neigh])
        
        return ans
            