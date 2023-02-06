class DetectSquares:

    def __init__(self):
        self.points = Counter({})

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        numRectangles = 0
        
        x2, y2 = point
        for x1, y1 in self.points.keys():
            if (abs(y2-y1) != abs(x2-x1)) or x1 == x2 or y1 == y2:
                continue
            numRectangles += self.points[(x1, y2)] * self.points[(x2, y1)] * self.points[(x1, y1)]

        return numRectangles


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)