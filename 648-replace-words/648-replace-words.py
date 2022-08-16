class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        
        curr.isWord = True
    
    def hasPrefix(self, word):
        curr = self.root

        for index, letter in enumerate(word):
            if curr.isWord == True:
                return word[:index]
            
            if letter not in curr.children:
                return word

            curr = curr.children[letter]
        
        return word
            
        
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        sentence = sentence.split()
        
        for word in dictionary:
            trie.insert(word)
        
        for i in range(len(sentence)):
            sentence[i] = trie.hasPrefix(sentence[i])

        return ' '.join(sentence)
        