class Allocator:

    def __init__(self, n: int):
        self.memory = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        left = 0
        n = len(self.memory)
        
        for i in range(n):
            # if curr is not free
            if self.memory[i] != 0:
                left = i + 1
                
            if i >= left and i - left + 1 == size:
                for j in range(left, i+1):
                    self.memory[j] = mID
                return left

        return -1

    def free(self, mID: int) -> int:
        n = len(self.memory)
        count = 0

        for i in range(n):
            if self.memory[i] == mID:
                count += 1
                self.memory[i] = 0
        
        return count


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)