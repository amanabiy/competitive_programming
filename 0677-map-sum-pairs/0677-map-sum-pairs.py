class Node: 
    def __init__(self, isEnd=False, value=0):
        self.isEnd = isEnd
        self.value = value
        self.child = {}
    

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, word, val):
        # O(len(word))
        curr = self.root

        for char in word:
            if char not in curr.child:
                curr.child[char] = Node()
            curr.value += val
            curr = curr.child[char]
        
        curr.isEnd = True
        curr.value += val
        
    def getSum(self, prefix):
        # O(lenWord * numWord)
        
        curr = self.root
        for char in prefix:
            if char not in curr.child:
                return 0
            curr = curr.child[char]
        
        return curr.value


class MapSum:

    def __init__(self):
        self.trie = Trie()
        self.word = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        newVal = val - self.word[key]
        self.word[key] = val
        self.trie.add(key, newVal)

    def sum(self, prefix: str) -> int:
        return self.trie.getSum(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)