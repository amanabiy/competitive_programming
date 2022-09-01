# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = [0]
        def dfs(node, maxx):
            if not node:
                return 0
            if node.val >= maxx:
                ans[0] += 1
            maxx = max(maxx, node.val)
            left = dfs(node.left, maxx)
            right = dfs(node.right, maxx)
            
        
        dfs(root, -inf)
        return ans[0]
            