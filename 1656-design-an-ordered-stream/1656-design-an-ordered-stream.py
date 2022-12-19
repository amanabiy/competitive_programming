class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 0
        self.arr = [""] * n

    def insert(self, idKey: int, value: str) -> List[str]:
        chunks = []
        idKey -= 1
        self.arr[idKey] = value
        if self.ptr == idKey:
            while self.ptr < len(self.arr) and self.arr[self.ptr]:
                chunks.append(self.arr[self.ptr])
                self.ptr += 1
        
        return chunks

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)