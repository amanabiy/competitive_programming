# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def backtrack(self, node, path, ans):
        if not node:
            return
        
        
        path.append(node.val)
        # if leaf append to ans
        if not node.left and not node.right:
            ans.append("->".join(map(str, path)))
        
        self.backtrack(node.left, path, ans)
        self.backtrack(node.right, path, ans)
        path.pop()
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        self.backtrack(root, [], ans)
        return ans
        