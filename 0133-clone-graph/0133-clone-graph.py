"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        
        """
        if not node:
            return None

        keyNode = {}
        queue = deque([node])
        
        while queue:
            currNode = queue.popleft()
            if currNode.val not in keyNode:
                keyNode[currNode.val] = Node(currNode.val)
            
            for child in currNode.neighbors:
                if child.val not in keyNode:
                    queue.append(child)
                    keyNode[child.val] = Node(child.val)
                
                keyNode[currNode.val].neighbors.append(keyNode[child.val])
    
        return keyNode[1]
        
        
        