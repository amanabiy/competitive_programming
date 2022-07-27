# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        if not root.left and  not root.right:
            return root

        right = self.flatten(root.right)
        left = self.flatten(root.left)
        root.left = None

        if left:
            root.right = left
            while left.right:
                left = left.right
            left.right = right
        else:
            root.right = right
       
        
        return root