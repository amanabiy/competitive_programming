class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        minHeap = []
        graph = defaultdict(list)
        knowSecret = {0: 0, firstPerson: 0}


        for p1, p2, t1 in meetings:
            graph[p1].append([t1, p2])
            graph[p2].append([t1, p1])


        minHeap = [[0, firstPerson], [0, 0]]


        while minHeap:
            time, person = heapq.heappop(minHeap)
            if time > knowSecret[person]:
                continue
            for t, ps in graph[person]:
                if t >= time and (ps not in knowSecret or (ps in knowSecret and t < knowSecret[ps])):
                    knowSecret[ps] = t
                    heapq.heappush(minHeap, [t, ps])


        return list(knowSecret.keys())