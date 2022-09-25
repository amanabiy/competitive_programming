class MyCircularQueue:

    def __init__(self, k: int):
        self.myQueue = []
        self.max = k
        self.size = 0
        

    def enQueue(self, value: int) -> bool:
        if self.size < self.max:
            self.myQueue.append(value)
            self.size += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.myQueue = self.myQueue[1:]
            self.size -= 1
            return True
        
        

    def Front(self) -> int:
        if self.myQueue:
            return self.myQueue[0]
        else:
            return -1
        

    def Rear(self) -> int:
        if self.myQueue:
            return self.myQueue[-1]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False
        
    def isFull(self) -> bool:
        if self.size == self.max:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()