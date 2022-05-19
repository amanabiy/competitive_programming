class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
           
    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.isWord = True        
    
    def search(self, word, isPrefix = False):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.isWord or isPrefix
    
    def startsWith(self, prefix):
        return self.search(prefix, True)
    
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        tree = Trie()
        tree.insert(s)
        count = 0
        for word in words:
            if tree.startsWith(word):
                count += 1
        return count
    