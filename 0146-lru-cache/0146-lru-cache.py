from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyValue = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.keyValue:
            return -1
        self.keyValue.move_to_end(key)
        return self.keyValue[key]

    def put(self, key: int, value: int) -> None:
        if key in self.keyValue:
            self.keyValue[key] = value
            self.keyValue.move_to_end(key)
            return
        if len(self.keyValue) == self.capacity:
            self.keyValue.popitem(last=False)
        self.keyValue[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)