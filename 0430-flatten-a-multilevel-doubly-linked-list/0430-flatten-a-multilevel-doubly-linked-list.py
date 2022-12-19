"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        root = head
        
        def dfs(node):
            if not node:
                return None
            
            child = dfs(node.child)
            nextTemp = node.next
            
            if child:
                # connect the child
                child.next = nextTemp
                if nextTemp:
                    nextTemp.prev = child
                node.next = node.child
                node.child.prev = node
                node.child = None

            nexts = dfs(nextTemp)            
            return nexts or nextTemp or child or node

        dfs(head)
        return root