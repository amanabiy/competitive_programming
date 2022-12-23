class Node:
    def __init__(self, key=None, val=None, nextP=None, prev=None):
        self.key = key
        self.val = val
        self.next = nextP
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addAtEnd(self, key, val):
        node = Node(key, val)
        if self.tail:
            node.prev = self.tail
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        return node
    
    def deleteFirst(self):
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
    
    def moveToLast(self, node):
        # if at the end or one
        if self.tail == node:
            return
    
        # if at the beggning
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        node.next.prev = node.prev
        
        # build connection with the tail
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = DoublyLinkedList()
        self.mapNodes = {}

    def get(self, key: int) -> int:
        if key not in self.mapNodes:
            return -1
        node = self.mapNodes[key]
        self.nodes.moveToLast(node)
        return node.val
        
    
    def put(self, key: int, value: int) -> None:
        if key in self.mapNodes:
            node = self.mapNodes[key]
            node.val = value
            self.nodes.moveToLast(node)
        else:
            if len(self.mapNodes) == self.capacity:
                del self.mapNodes[self.nodes.head.key]
                self.nodes.deleteFirst()
            self.mapNodes[key] = self.nodes.addAtEnd(key, value)
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)