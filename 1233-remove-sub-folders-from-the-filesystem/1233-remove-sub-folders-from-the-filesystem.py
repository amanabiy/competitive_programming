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
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.isWord = True        

    def allRootFolders(self):
        ans = []
        def dfs(node, strs):
            # if not node.children:
            #     return
            if node.isWord:
                ans.append("/".join(strs))
            else:
                for key in node.children:
                    dfs(node.children[key], strs+[key])
        dfs(self.root, [])
        return ans

    
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folders = Trie()
        ans = []
        
        for f in folder:
            if f != '' and f != '/':
                folders.insert(f)
        
        return folders.allRootFolders()