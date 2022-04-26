class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ans = [set() for i in range(n)]
        incoming = { i: 0 for i in range(n) }
        graph = defaultdict(list)
        queue = deque()
        
        for come, to in prerequisites:
            incoming[to] += 1
            graph[come].append(to)
        
        for keys in incoming.keys():
            if incoming[keys] == 0:
                queue.append(keys)
        
        while queue:
            node = queue.popleft()
            for neigh in graph[node]:
                ans[neigh] = ans[neigh] | (ans[node])
                ans[neigh].add(node)
                incoming[neigh] -= 1
                if incoming[neigh] == 0:
                    queue.append(neigh)
        soln = []      
        for i, j in queries:
            soln.append(i in ans[j])
    
        return soln