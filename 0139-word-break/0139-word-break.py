class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        cats -> catsandog
                         |
        og
        """
        def dfs(i, trie, s, memo):
            if i >= len(s):
                return True
            
            if i in memo:
                return memo[i]
            
            # search for a word from my trie
            curr = trie
            while i < len(s) and s[i] in curr.children:
                curr = curr.children[s[i]]
                i += 1
                if curr.isEnd:
                    ans = dfs(i, trie, s, memo)
                    if ans:
                        return True

            memo[i] = False
            return False
        
        trie = TrieNode()

        for word in wordDict:
            curr = trie
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                # print(curr.children, curr.isEnd)
                curr = curr.children[c]
            curr.isEnd = True
        
        return dfs(0, trie, s, {})