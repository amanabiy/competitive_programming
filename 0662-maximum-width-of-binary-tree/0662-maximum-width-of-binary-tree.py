# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
            1
        3       2
    5               9
"""
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        queue = deque([[root, 0, 1]])
        
        
        while queue:
            mostLeft = float('inf')
            mostRight = float('-inf')
            count = 0

            for _ in range(len(queue)):
                node, before, pos = queue.popleft()
                mostLeft = min(pos, mostLeft)
                mostRight = max(pos, mostRight)
                if node.left:
                    queue.append((node.left, before, (pos * 2) + 1))
                if node.right:
                    queue.append((node.right, before, (pos) * 2))
                count += 1

            ans = max(ans, (mostRight - mostLeft + 1))
            
        return ans
                        
            
            