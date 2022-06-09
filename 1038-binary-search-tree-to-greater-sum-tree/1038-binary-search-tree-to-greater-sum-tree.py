# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        
        def dfs(node, value):
            if not node:
                return value
            
            if not node.left and not node.right:
                node.val += value
                return node.val
            
            right = dfs(node.right, value)
            node.val = right + node.val
            
            left = dfs(node.left, node.val)
            node.val
            
            return max(node.val, left)

        
        dfs(root, 0)
        return root