class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:

        def calcDist(p1, p2):
            a = (p1[0] - p2[0]) ** 2
            b = (p1[1] - p2[1]) ** 2
            return sqrt(a + b)
        
        ans = []

        for x, y, r in queries:
            count = 0
            for t, s in points:
                dist = calcDist((x, y), (t, s))
                if dist <= r:
                    count += 1            
            ans.append(count)
        
        return ans
            