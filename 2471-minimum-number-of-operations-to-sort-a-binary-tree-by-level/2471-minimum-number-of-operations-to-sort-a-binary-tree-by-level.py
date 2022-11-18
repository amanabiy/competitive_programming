# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        minOperation = 0
        queue = deque([root])

        while queue:
            newLevel = []
            # create a new level
            for elem in queue:
                if elem.left:
                    newLevel.append(elem.left)
                if elem.right:
                    newLevel.append(elem.right)
            
            # process cost each level I have in the queue to be sorted
            heap = [node.val for node in queue]
            heapq.heapify(heap)
            index = {node.val: i for i, node in enumerate(queue)}

            for i, element in enumerate(queue):
                if element.val != heap[0]:
                    index[element.val] = index[heap[0]]
                    index[heap[0]] = i
                    queue[i], queue[index[element.val]] = queue[index[element.val]], queue[i]
                    minOperation += 1
                heapq.heappop(heap)
            
            queue = newLevel

        return minOperation