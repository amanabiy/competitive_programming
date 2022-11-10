# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return [ float('-inf'), float('-inf') ] # [maxPath, ans]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            maxPath = max(left[0] + node.val, right[0] + node.val, node.val)            
            maxAnswer = max(left[0] + right[0] + node.val, maxPath, left[1], right[1])
            
            return [maxPath, maxAnswer]
        
        return dfs(root)[1]
            
            