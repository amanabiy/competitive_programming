class Solution:               
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        heap = []
        ans = float('-inf')
        curr = 0
        events.sort()
        
        for i in range(len(events)):
            s, e, val = events[i]
            while heap and heap[0][0] < s:
                curr = max(curr, heapq.heappop(heap)[1])
            ans = max(ans, val + curr)
            heapq.heappush(heap, (e, val))
            
        return ans