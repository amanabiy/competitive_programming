# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        roots = []
        to_delete = set(to_delete)
        def dfs(node):
            if not node:
                return None
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            if node.val in to_delete:
                if node.left:
                    roots.append(node.left)
                if node.right:
                    roots.append(node.right)
                return None
            
            return node
        
        dfs(root)
        if root.val not in to_delete:
            roots.append(root)

        return roots