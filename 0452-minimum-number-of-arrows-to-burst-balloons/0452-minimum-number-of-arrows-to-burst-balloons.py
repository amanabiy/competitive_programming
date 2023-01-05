class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        end = float('-inf')
        count = 0
        n = len(points)

        points.sort()
        for i in range(n):
            if end < points[i][0]:
                count += 1
                end = points[i][1]
            else:
                end = min(end, points[i][1])

        return count