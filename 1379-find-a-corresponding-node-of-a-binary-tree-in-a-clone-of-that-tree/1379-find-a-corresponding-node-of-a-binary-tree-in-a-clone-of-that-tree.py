# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        
        def dfs(org, clon):
            nonlocal target
            if not org:
                return None
            if target == org:
                return clon
            left = dfs(org.left, clon.left)
            right = dfs(org.right, clon.right)
            
            return left or right
        
        return dfs(original, cloned)