class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        """
        [1,2,4,4,3]
        [1,3,4,1,3]
        
        [2, 2, 2, 1]
        [1, 1, 1, 1]
        
        
        """
        heap = []
        skip = set()
        
        for i in range(len(fronts)):
            if (fronts[i] not in skip or backs[i] not in skip) and fronts[i] != backs[i]:
                heapq.heappush(heap, fronts[i])
                heapq.heappush(heap, backs[i])
            else:
                skip.add(fronts[i])
        
        while heap:
            ans = heapq.heappop(heap)
            if ans not in skip:
                return ans
        
        return 0
        