class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            x, y = intervals[i]
            if x <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], y)
            else:
                ans.append([x, y])
        
        return ans
        