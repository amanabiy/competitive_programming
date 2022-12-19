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
        stack = []
        currNode = head
        prev = None

        while currNode or stack:
            if currNode:
                if currNode.child:
                    if currNode.next:
                        stack.append(currNode.next)
                    currNode.next = currNode.child
                    child = currNode.child
                    currNode.child.prev = currNode
                    currNode.child = None
                    prev, currNode = currNode, child
                else:
                    prev, currNode = currNode, currNode.next
            else:
                node = stack.pop()
                prev.next = node
                node.prev = prev
                currNode = node
        
        return head