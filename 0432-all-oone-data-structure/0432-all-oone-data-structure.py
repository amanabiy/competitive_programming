class Node:
    def __init__(self, key="", val = None, next = None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev



class AllOne:

    def __init__(self):
        self.head = Node()
        self.tail = Node("", None, None, self.head)
        self.head.next = self.tail
        self.keys = Counter()
        self.nodePtr = {}
        
    def swap(self, back, front):
        # connect front with back of back
        back.prev.next = front
        front.prev = back.prev
        
        # connect back forward
        back.next = front.next
        front.next.prev = back
        
        # connect front forward and back backward
        front.next = back
        back.prev = front        
        

    def inc(self, key: str) -> None:
        self.keys[key] += 1
        if self.keys[key] == 1:
            newNode = Node(key, 0, self.head.next, self.head)
            self.nodePtr[key] = newNode
            self.head.next.prev = newNode
            self.head.next = newNode

        node = self.nodePtr[key]
        node.val += 1
        while node.next.val and node.val > node.next.val:
            # swap the two place
            self.swap(node, node.next)
        
    def dec(self, key: str) -> None:
        self.keys[key] -= 1
        node = self.nodePtr[key]
        node.val -= 1
        if self.keys[key] == 0:
            del self.nodePtr[key]
            del self.keys[key]
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            while node.prev.val and node.prev.val > node.val:
                # swap the two place
                self.swap(node.prev, node)

    def getMaxKey(self) -> str:
        return self.tail.prev.key 

    def getMinKey(self) -> str:
        return self.head.next.key


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()