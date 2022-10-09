class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
           
    def insert(self, word):
        current = self.root
        word = word.split('/')
        
        for char in word:
        
            if current.isWord:
                return False
            
            if char not in current.children:
                current.children[char] = TrieNode()
            
            current = current.children[char]

        current.isWord = True
        return True


    
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        folders = Trie()
        ans = []
        
        for f in folder:
            if f != '' and f != '/':
                if folders.insert(f):
                    ans.append(f)
        return ans
        
        # return folders.allRootFolders()