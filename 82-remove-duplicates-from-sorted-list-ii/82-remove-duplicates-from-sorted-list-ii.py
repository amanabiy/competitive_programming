# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, node: Optional[ListNode]) -> Optional[ListNode]:
        """
        Duplication at the begining:
        1 -> 1 -> 2 -> 3
        |    |
        head -> 2
        Duplication at the middle:
        1 -> 2 -> 2 -> 3
        |    |
        Duplication at the end:
        """
        def remove(head):
            if not head:
                return [None, float('inf')]
            if head:
                next_node = remove(head.next)

                if next_node[1] == head.val:
                    node_to_return = None
                    if next_node[0] and next_node[0].val == head.val:
                        node_to_return = next_node[0].next if next_node[0] and next_node[0] else None
                    else:
                        node_to_return = next_node[0]
                    return [node_to_return, next_node[1]]
                
                else:
                    head.next = next_node[0]
                    return [head, head.val]
            
        return remove(node)[0]
        # if next_node and next_node.val == head.val:
            
            
        