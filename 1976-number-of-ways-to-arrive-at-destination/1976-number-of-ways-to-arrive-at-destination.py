class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        dp = [inf] * n 
        shortestTime = [inf] * n
        ans = 0
        heap = []

        for i, j, k in roads:
            graph[i].append((j, k))
            graph[j].append((i, k))
    
        heap.append((0, 0))
        dp[0] = 1

        while heap:

            Times, node = heapq.heappop(heap)            

            if node == n - 1:
                return dp[-1]

            # if shortestTime[node] < Times:
            #     continue
        
            # shortestTime[node] = Times

            for child, time in graph[node]:
                if shortestTime[child] > time + Times:
                    heapq.heappush(heap, (Times + time, child))
                    shortestTime[child] = time + Times
                    dp[child] = dp[node]
                elif shortestTime[child] == time + Times:
                    dp[child] = (dp[child] + dp[node]) % (10 ** 9 + 7) 
                    
                        
