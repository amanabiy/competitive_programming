class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        incoming = defaultdict(int)
        graph = defaultdict(list)
        queue = deque()
        ans = []
        
        for i in range(numCourses):
            incoming[i] = 0
        
        for dest, pre in prerequisites:
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

        return ans if len(incoming.keys()) == len(ans) else []