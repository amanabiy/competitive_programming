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
            curr = curr.child[char]
        
        curr.isEnd = True
        curr.value = val
        
    def getSum(self, prefix):
        # O(lenWord * numWord)
        
        curr = self.root
        for char in prefix:
            if char not in curr.child:
                return 0
            curr = curr.child[char]
        
        return self.dfs(curr)
    
    def dfs(self, node):
        if not node:
            return 0
        
        ans = node.value
        
        for child in node.child:
            ans += self.dfs(node.child[child])
        
        return ans

class MapSum:

    def __init__(self):
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.add(key, val)

    def sum(self, prefix: str) -> int:
        return self.trie.getSum(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)