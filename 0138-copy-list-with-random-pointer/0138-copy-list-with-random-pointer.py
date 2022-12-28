"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Iterate and create nodes linking them with the next and random
        I will map each created node with the older one
        if the next is created by random I won't create again
        """
        if not head:
            return

        oldNew = defaultdict(lambda: Node(0))
        newNode = Node(head.val, None, None)
        curr = newNode
        
        while head:
            oldNew[head] = curr
            if head.random:
                curr.random = oldNew[head.random]
            if head.next:
                curr.next = oldNew[head.next]

            curr.val = head.val

            # Move curr to next and head to next too
            curr = curr.next
            head = head.next
        
        return newNode