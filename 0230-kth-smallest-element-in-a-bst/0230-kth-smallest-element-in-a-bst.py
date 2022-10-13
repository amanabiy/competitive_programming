# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = -1
        
        def dfs(node, less):
            if not node:
                return 0

            left = dfs(node.left, less) + 1
            if left + less == k and self.ans == -1:
                self.ans = node.val
            right = dfs(node.right, left + less)
            return left + right
        
        dfs(root, 0)
        return self.ans