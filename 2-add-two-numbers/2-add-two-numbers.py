# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        
        """
        
        ans = ListNode()

        curr = ans
        extra = 0
        
        while l1 or l2:
            val1 = val2 = sums = 0
            
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            
            sums = val1 + val2 + extra

            if sums > 9:
                sums = ((val1) + (val2) + extra) % 10
                extra = 1
            else:
                extra = 0

            curr.next = ListNode(sums)
            curr = curr.next

        if extra:
            curr.next = ListNode(extra)

        return ans.next
        