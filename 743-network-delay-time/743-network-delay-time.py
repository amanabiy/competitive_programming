class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        
        for i,j,w in times:
            graph[i].append((j,w))
        
        
        
        
        _min = [float("inf")] * (n + 1)
        visited = set()
        _min[k] = 0
        _min[0] = 0
        q = deque([k])
        not_visited = [[_min[k], k]]
        
        
        while not_visited:
            distance, node = heapq.heappop(not_visited)
            _min[node] = min(distance, _min[node])
            visited.add(node)
            
            
            for child, weight in graph[node]:
                if child not in visited:
                    heapq.heappush(not_visited, [distance + weight, child])
            # print(not_visited)
        print(_min)
        ans =  max(_min)
        if ans != float("inf"): return ans
        else:
            return -1
        
        
        
        