# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        root = ListNode()
        
        for i in range(len(lists)):
            val = lists[i].val if lists[i] else float('inf')
            heapq.heappush(heap, [val, i, lists[i]])
        curr = root
        while heap:
            # pop the min val heap
            val,i,node = heapq.heappop(heap)
            curr.next = node
            if node and node.next:
                node = node.next
                heapq.heappush(heap, [node.val,i, node])
            if curr and curr.next:
                curr = curr.next

        return root.next