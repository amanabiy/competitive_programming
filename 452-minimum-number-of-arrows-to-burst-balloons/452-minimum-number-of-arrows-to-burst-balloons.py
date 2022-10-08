class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        ans = 0
        last_ending = float('-inf')
        
        for i in range(len(points)):
            if points[i][0] > last_ending:
                last_ending = points[i][1]
                ans += 1
        
        return ans
        
        
        