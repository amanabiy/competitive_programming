class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.num = -1
    
class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        curr = self.root

        for i in range(31, -1, -1):
            node = num & (1<<i)
            node = 1 if node else 0
            
            if not curr.children[node]:
                curr.children[node] = TrieNode()

            curr = curr.children[node]
        
        curr.num = num
    
    def highestXOR(self, num):
        curr = self.root
        
        for i in range(31, -1, -1):
            node = num & (1 << i)
            node = 1 if not node else 0
        
            if curr.children[node]:
                curr = curr.children[node]
            else:
                curr = curr.children[int(not node)]
        
        return curr.num ^ num
    
    def findMaximumXOR(self, nums: List[int]) -> int:

        for num in nums:
            self.insert(num)

        ans = 0
        for num in nums:
            ans = max(ans, self.highestXOR(num))
            
        return ans