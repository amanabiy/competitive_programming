# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIdx = { val: i for i, val in enumerate(inorder) }
        i = 0
        # preorder = list(reversed(preorder))
        def dfs(start, end):
            nonlocal i
            if start > end or i >= len(preorder):
                return None
            
            index = inorderIdx[preorder[i]]

            node = TreeNode(preorder[i])
            i += 1

            node.left = dfs(start, index - 1)
            node.right = dfs(index + 1, end)

            return node
            # return None        
        return dfs(0, len(inorder) - 1)