# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(node):
            if not node:
                return [inf, -inf, 0]
            
            # if leaf node consider it as valid bst
            if not node.left and not node.right:
                self.ans = max(node.val, self.ans)
                return [node.val] * 3
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            weight = float('-inf')
            minn = inf
            maxx = -inf
            
            # check if right is valid bst and check if left is valid bst
            # print(node.val, left, right)
            if left[1] < node.val and right[0] > node.val:
                weight = left[2] + node.val
                minn = min(left[0], right[0], node.val)
                weight += right[2]
                maxx = max(right[1], left[1], node.val)
                self.ans = max(self.ans, weight)
                # print(node.val, "isvalid")

            # print(node.val, [minn, maxx, weight])
            return [minn, maxx, weight]
        
        dfs(root)
        return self.ans
            
            