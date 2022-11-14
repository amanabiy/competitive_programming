class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        heap = [(0, headID)]
        ans = 0

        for i in range(n):
            if i != headID:
                graph[manager[i]].append(i)

        while heap:
            maxTime = 0
            time, node = heapq.heappop(heap) 
            ans = max(ans, time)
            for child in graph[node]:
                heapq.heappush(heap, (time + informTime[node], child))


        return ans
        