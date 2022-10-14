class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        """
        graph = defaultdict(list)
        indegree = defaultdict(int)
        visited = set()
        queue = deque()
        
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
            indegree[n1] += 1
            indegree[n2] += 1
        
        for i in range(n):
            if indegree[i] == 1:
                queue.append(i)
                visited.add(i)
    
        ans = []
        # print(queue, indegree)
        while queue:
            n = len(queue)
            # indegree[n] -= 1
            ans = list(queue)

            for _ in range(n):
                node = queue.popleft()
                for neigh in graph[node]:
                    if neigh not in visited:
                        indegree[neigh] -= 1
                        if indegree[neigh] <= 1:
                            queue.append(neigh)
                            visited.add(neigh)
            # print(queue, indegree)

        # for i in range(n):
        #     if indegree[i] == 0:
        #         ans.append(i)
        return ans if ans else [0]