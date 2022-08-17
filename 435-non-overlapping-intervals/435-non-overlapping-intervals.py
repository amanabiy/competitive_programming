class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        curr, nexts = 0, 1
        ans = 0
        
        while nexts < len(intervals):
            if intervals[curr][1] <= intervals[nexts][0]:
                curr = nexts
                nexts += 1
                continue
            
            if intervals[curr][1] > intervals[nexts][1]:
                curr = nexts

            nexts += 1
            ans += 1
        
        return ans