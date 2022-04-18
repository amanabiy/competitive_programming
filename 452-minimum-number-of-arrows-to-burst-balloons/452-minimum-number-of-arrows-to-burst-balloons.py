class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)
        minn = points[0][0]
        maxx = points[0][1]
        count = 1
        for i in range(1, len(points)):
            curr_left, curr_right = points[i]
            if curr_left <= maxx and maxx <= curr_right or \
                minn <= curr_left and maxx >= curr_right:
                minn = max(curr_left, minn)
                maxx = min(curr_right, maxx)
            else:
                minn = curr_left
                maxx = curr_right
                count += 1
        return count