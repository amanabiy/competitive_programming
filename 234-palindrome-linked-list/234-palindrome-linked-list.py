# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 1 2 3 4
"""
1 2 3 4
        |
    |
"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def reverse(prev, curr):
            if not curr:
                return prev
            temp = curr.next
            curr.next = prev
            return reverse(curr, temp)
        
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        middle = reverse(None, slow)
        while middle:
            if middle.val != head.val:
                return False
            middle, head = middle.next, head.next
        
        return True