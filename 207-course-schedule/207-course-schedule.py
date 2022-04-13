class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        incoming = defaultdict(int)
        graph = defaultdict(list)
        queue = deque()
        ans = []
        
        for pre, dest in prerequisites:
            if pre not in incoming:
                incoming[pre] = 0
            if dest not in incoming:
                incoming[dest] = 0
            graph[pre].append(dest)
            incoming[dest] += 1

           
        for key in incoming.keys():
            if incoming[key] == 0:
                queue.append(key)

        while queue:
            node = queue.popleft()
            ans.append(node)
            for neighbor in graph[node]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    queue.append(neighbor)

        return len(incoming.keys()) == len(ans)