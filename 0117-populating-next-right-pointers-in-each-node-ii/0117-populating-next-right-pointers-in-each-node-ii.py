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
    def connect(self, root: 'Node') -> 'Node':

        def findMostRight(node):
            if not node:
                return None
            return node.left or node.right or findMostRight(node.next)
        
        def dfs(node, parent):
            if not node:
                return None

            if parent and parent.right and parent.right != node:
                node.next = parent.right
            else:
                parent = parent if not parent else parent.next
                node.next = findMostRight(parent)

            right = dfs(node.right, node)
            left = dfs(node.left, node)

        dfs(root, None)
        return root