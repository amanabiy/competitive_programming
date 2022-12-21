class StockPrice:

    def __init__(self):
        self.stock = {}
        self.max = []
        self.min = []
        self.latest = []
        

    def update(self, timestamp: int, price: int) -> None:
        if timestamp not in self.stock:
            heapq.heappush(self.latest, -timestamp)
        self.stock[timestamp] = price
        heapq.heappush(self.max, (-price, timestamp))
        heapq.heappush(self.min, (price, timestamp))

    def current(self) -> int:
        return self.stock[-self.latest[0]]

    def maximum(self) -> int:
        while self.stock[self.max[0][1]] != (self.max[0][0] * -1):
            heapq.heappop(self.max)
        return (self.max[0][0] * -1)

    def minimum(self) -> int:
        while self.stock[self.min[0][1]] != self.min[0][0]:
            heapq.heappop(self.min)
        return self.min[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()