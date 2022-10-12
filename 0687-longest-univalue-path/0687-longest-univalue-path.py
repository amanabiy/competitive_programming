# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node): # return the ["currMax", "The global max Until now"]
            if not node:
                return [0, 0]
            left, right = [0, 0], [0, 0]
            left = dfs(node.left)
            right = dfs(node.right)
            maxIcanMake = 0
            globalMax = max(left[1], right[1])
            if node.left and node.left.val == node.val:
                maxIcanMake = left[0]
                globalMax = max(globalMax, left[0] + 1)
            if node.right and node.right.val == node.val:
                maxIcanMake = max(right[0], maxIcanMake)
                
            globalMax = max(globalMax, maxIcanMake)
            if node.right and node.left:
                if node.left.val == node.right.val == node.val:
                    globalMax = max(left[0] + right[0] + 1, globalMax)

            globalMax = max(globalMax, maxIcanMake + 1)
            # print(node.val, maxIcanMake + 1, globalMax)
            return [maxIcanMake + 1, globalMax]
        
            
            
        return dfs(root)[1] - 1