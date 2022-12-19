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
            
            currNode = node
            nextTemp = node.next
            prev = None
    
            while currNode:
                if currNode.child:
                    tail = dfs(currNode.child)
                    tail.next = currNode.next
                    if currNode.next:
                        currNode.next.prev = tail
                    currNode.next = currNode.child
                    currNode.child.prev = currNode
                    currNode.child = None
                    currNode = tail.next
                    prev = tail
                else:
                    prev, currNode = currNode, currNode.next
            
            return prev

        dfs(head)
        return root