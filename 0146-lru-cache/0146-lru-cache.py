class Node:
    def __init__(self, key=None, val=None, nextP=None, prev=None):
        self.key = key
        self.val = val
        self.next = nextP
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add(self, key, val):
        lastNode = self.tail.prev
        newNode = Node(key, val)
        newNode.next = lastNode.next
        lastNode.next = newNode
        newNode.prev = lastNode
        self.tail.prev = newNode
        return newNode
        
    def delete(self, node):
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev
        del node
    
    def getFrist(self):
        if self.head.next != self.tail:
            return self.head.next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = DoublyLinkedList()
        self.mapNodes = {}

    def get(self, key: int) -> int:
        if key not in self.mapNodes:
            return -1
        node = self.mapNodes[key].val
        self.nodes.delete(self.mapNodes[key])
        self.mapNodes[key] = self.nodes.add(key, node)
        return node
    
    def put(self, key: int, value: int) -> None:
        if key in self.mapNodes:
            self.nodes.delete(self.mapNodes[key])
        if len(self.mapNodes) == self.capacity and key not in self.mapNodes:
            self.mapNodes.pop(self.nodes.head.next.key)
            self.nodes.delete(self.nodes.head.next)
        self.mapNodes[key] = self.nodes.add(key, value)
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)