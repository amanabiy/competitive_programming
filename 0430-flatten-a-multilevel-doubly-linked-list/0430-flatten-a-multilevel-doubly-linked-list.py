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
            temp = node.next
            x = None      
            if child:
                node.next = node.child
                node.child.prev = node
                child.next = temp
                node.child = None
                if temp:
                    temp.prev = child
                else:
                    return child
            
            x = dfs(temp)
            if x == None:
                return node

            return x
        
        dfs(head)
        return root