class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        queue = deque()
        ans = [ i for i in range(len(quiet)) ]
        
        for rich, poor in richer:
            graph[rich].append(poor)
            indegree[poor] += 1
        
        for key in graph:
            if indegree[key] == 0:
                queue.append(key)
        
        while queue:
            node = queue.popleft()
            for neigh in graph[node]:
                indegree[neigh] -= 1
                
                if quiet[ans[neigh]] > quiet[ans[node]]:
                    ans[neigh] = ans[node]
                
                if indegree[neigh] == 0:
                    queue.append(neigh)
        
        return ans
        
        