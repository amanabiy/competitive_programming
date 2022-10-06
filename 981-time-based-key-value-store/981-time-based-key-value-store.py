class TimeMap:
    """
    key -> timeStamp -> value
    key -> (timeStamp, value)
    
    [(1, bar), ()]
    
    timeStamp -> search if you don't get it you return the earliest or the closest you find
    Time: O(timeStamp * queries) -> O(Qlogn(n))
    Space: O(n)
    """
    def __init__(self):
        self.store = defaultdict(list)        

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        For each set operation
        Time: O(1)
        Space: O(n)
        """
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """ For each get request
        Time: O(log(n))
        Space: O(1)
        """
        
        # get the values with same key
        values = self.store[key]
        
        # try to find the most left position you could for the timestamp using binary search
        left = 0
        right = len(values)
        ans = -1
    
        while left < right:
            mid = left + (right - left) // 2

            if values[mid][0] <= timestamp:
                ans = mid
                left = mid + 1
            else:
                right = mid
        
        foundValue = values[mid][1] if ans != -1 else ""
        return foundValue

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)