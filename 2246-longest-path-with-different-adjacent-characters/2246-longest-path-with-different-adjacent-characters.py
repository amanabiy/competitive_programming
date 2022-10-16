class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        """
        
            0
          3
        1 3 2
          3   4
        """
        n = len(parent)
        visited = set()
        queue = deque()
        graph = defaultdict(list)
        ans = [ 1 for _ in range(n) ]
        indegree = [ 0 for _ in range(n) ]
        maxAns = 1

        for i in range(1, n):
            graph[parent[i]].append(i)
            graph[i].append(parent[i])
            indegree[parent[i]] += 1
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                visited.add(i)
        # print("queue", queue, indegree)
        while queue:
            n = queue.popleft()

            for neigh in graph[n]:
                if neigh not in visited :
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        # print(ans[neigh])
                        queue.append(neigh)
                        visited.add(neigh)
                    if s[neigh] != s[n]:
                        maxAns = max(ans[neigh] + ans[n], maxAns)
                        ans[neigh] = max(ans[neigh], ans[n] + 1)
        # print(ans, indegree, maxAns)
        return maxAns