class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        y - y1  = m
        x - x1
        
        vertical -> x would be zero
        horizontal -> y would be zero
        """
        ans = 0
        
        def slopBetweenPoints(p1, p2):
            if p2[0] - p1[0] == 0:
                return float('inf')
            return (p2[1] - p1[1]) / (p2[0] - p1[0])
        
        for i in range(len(points)):
            slopes = defaultdict(int)
            for j in range((len(points))):
                if i != j:
                    s = slopBetweenPoints(points[i], points[j])
                    slopes[s] += 1
            ans = max(ans, max(list(slopes.values()) + [0]) + 1)
        
        return ans