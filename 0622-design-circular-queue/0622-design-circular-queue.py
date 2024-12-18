class MyCircularQueue:

    def __init__(self, k: int):
        self.myQueue = [-199] * k
        self.front = -1
        self.size = k
        self.rear = 0
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.front == -1:
            self.front += 1
        self.myQueue[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.myQueue[self.front] = -199
        self.front = (self.front + 1) % self.size
        if self.front == self.rear:
            self.front = -1
            self.rear = 0
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.myQueue[self.front]
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.myQueue[self.rear - 1]
        

    def isEmpty(self) -> bool:
        if self.front == -1:
            return True
        return False
        
    def isFull(self) -> bool:
        if self.rear == self.front:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()