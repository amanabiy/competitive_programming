class DetectSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] = self.points.get(tuple(point), 0) + 1
        return

    def is_square(self, xi, yi, xf, yf)->None:
        return not (xi == xf or yi == yf or abs(xi - xf) != abs(yi - yf))

    def count(self, point: List[int]) -> int:
        count = 0
        for xf, yf in self.points:
            xi, yi = point
            if self.is_square(xi, yi, xf, yf):
                count += self.points.get((xi, yf), 0) * self.points.get((xf, yi), 0) * self.points.get((xf, yf), 0)
    
        return count

        
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)