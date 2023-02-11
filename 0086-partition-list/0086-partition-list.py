# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        ls = less
        large = ListNode()
        g = large
        
        while head:
            if head.val < x:
                ls.next = head
                ls = ls.next
            else:
                g.next = head
                g = g.next
            head = head.next
        
        g.next = None
        ls.next = large.next
        return less.next