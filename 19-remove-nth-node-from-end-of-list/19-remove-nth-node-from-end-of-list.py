# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return head.next

        fast = slow = head
        i = 0
        
        while i < n and fast:
            fast = fast.next
            i += 1
        
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
            i += 1

        # print(slow, fast, n, i, i)
        if not fast:
            head = head.next
        else:
            slow.next = slow.next.next
        
        return head
        