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
    
    def isSubSequence(self, word):
        current = self.root
        for char in word:
            while char not in current.children:
                if not current.children:
                    return False
                for key in current.children:
                    # print(key, current.children)
                    current = current.children[key]
            for key in current.children:
                # print(key, current.children)
                current = current.children[key]
        return True
    
    def search(self, word, isPrefix = False):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.isWord or isPrefix
    
    # def populate
    
    def startsWith(self, prefix):
        return self.search(prefix, True)
    
    def letter(self, l, node):
        current = self.root
        current.children[l] = node
    
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        node = Trie()
        node.insert(s)
        count = 0
        
        # @lru_cache(maxsize=None)
        # def builTrie(i, strin):
        #     nonlocal s
        #     print(i, strin)
        #     if i < len(s):
        #         for index in range(i, len(s)):
        #             for j in range(index + 1, len(s)):
        #                 new_str = strin + s[index] + s[j]
        #                 node.insert(new_str)
        #                 # node.insert()
        #                 # node.insert(s[i] + s[j])
        #                 print(index, j, new_str)
        #                 builTrie(j, new_str + s[index])
        # builTrie(0, "")
    
        memo = {}
        for word in words:
            if word not in memo:
                memo[word] = node.isSubSequence(word)
            count += 1 if memo[word] else 0
            
        return count
        