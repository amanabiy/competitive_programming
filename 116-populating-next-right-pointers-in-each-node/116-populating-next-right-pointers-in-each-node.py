"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        
        def dfs(node, right):
            if node:
                
                # left
                node.next = right
                dfs(node.left, node.right)
                right = right.left if right else None
                dfs(node.right, right)
        
        dfs(root, None)
        return root