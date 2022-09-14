# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, values):
            if not node: return 0
            values[node.val] += 1
            if not node.left and not node.right:
                count = 0
                ret = 1
                for key in values:
                    if values[key] % 2 == 1:
                        count += 1
                    if count > 1:
            
                        ret = 0
                values[node.val] -= 1
                return ret

            left = dfs(node.left, values)
            right = dfs(node.right, values)
            values[node.val] -= 1
            
            return left + right
        
        return dfs(root, defaultdict(int))
            
            
            
        