# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        stack1 = []
        stack2 = []
        
        while l1 or l2:
            if l1:
                stack1.append(l1.val)
                l1 = l1.next
            if l2:
                stack2.append(l2.val)
                l2 = l2.next
        
        last = None
        newNode = None
        while stack1 or stack2 or remainder:
            v1 = stack1.pop() if stack1 else 0
            v2 = stack2.pop() if stack2 else 0
            totalSum = v1 + v2 + remainder
            remainder = 1 if totalSum > 9 else 0
            newNode = ListNode((totalSum) % 10, last)
            last = newNode
        
        return newNode