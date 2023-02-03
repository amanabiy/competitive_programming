# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        column = defaultdict(list)
        queue = deque([[0, 0, root]])
        
        while queue:
            n = len(queue)
            same_row = defaultdict(list)
            for i in range(n):
                row, col, node = queue.popleft()
                same_row[col].append(node.val)
                if node.left:
                    queue.append([row + 1, col - 1, node.left])
                if node.right:
                    queue.append([row + 1, col + 1, node.right])
            
            for key in same_row:
                column[key].extend(sorted(same_row[key]))
                
        return [column[key] for key in sorted(column.keys())]