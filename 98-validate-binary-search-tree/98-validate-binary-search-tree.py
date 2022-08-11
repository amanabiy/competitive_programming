# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validateBST(node, smaller, higher):
            if not node:
                return True
            if node.val <= smaller or node.val >= higher:
                return False
            
            left = validateBST(node.left, smaller, node.val)
            right = validateBST(node.right, node.val, higher)
            
            return left and right
        
        return validateBST(root, -inf, inf)
        