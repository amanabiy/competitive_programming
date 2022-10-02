# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        
        def dfs(node, canRob):
            if not node:
                return 0
            
            if (node, canRob) in memo:
                return memo[(node, canRob)]
            
            robbed = 0
            
            if canRob:
                robbed += node.val

            isRobbed = dfs(node.left, not canRob) + dfs(node.right, not canRob) + robbed
            notRobbed = dfs(node.left, canRob) + dfs(node.right, canRob)
            
            memo[(node, canRob)] = max(isRobbed, notRobbed)
            return memo[(node, canRob)]
        
        return dfs(root, True)
                