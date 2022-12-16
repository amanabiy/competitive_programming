class Solution:
    def right(self, arr, val):
        lo = 0
        hi = len(arr) - 1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] <= val:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return lo
                
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        prefixSum = [0]
        ans = float('-inf')
        events.sort()
        startTime = [s for s, e, v in events]
        
        for i in range(len(events) - 1, -1, -1):
            prefixSum.append(max(prefixSum[-1], events[i][2]))
        
        prefixSum = prefixSum[::-1]
        for i in range(len(events)):
            index = self.right(startTime, events[i][1])
            ans = max(ans, prefixSum[index] + events[i][2])
        
        return ans