class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        visited = {source}
        visitedBus = set()
        queue = deque([source])
        path = defaultdict(list)
        step = 0

        for i, bus in enumerate(routes):
            for n in bus:
                path[n].append(i)

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node == target:
                    return step

                for ind in path[node]:
                    if ind in visitedBus:
                        continue
                    for route in routes[ind]:
                        if route not in visited:
                            visited.add(route)
                            queue.append(route)
                    visitedBus.add(ind)

            step += 1
        
        return -1