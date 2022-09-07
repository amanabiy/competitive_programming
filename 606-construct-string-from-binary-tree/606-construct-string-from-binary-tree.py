# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node:
                return ""
            
            ans = str(node.val)
            left = dfs(node.left)
            right = dfs(node.right)

            if right:
                ans = ans + "(" + left + ")" +  "(" + right + ")"
            elif left:
                ans = ans + "(" + left + ")"
            
            return ans
            


        return dfs(root)