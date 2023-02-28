# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.count = []
        self.taken = set()
        
        
        def dfs(node, seen):
            if not node:
                return '@'
            
            left = dfs(node.left, seen)
            right = dfs(node.right, seen)
            
            encode = left + "#" + right + "#" + f"{node.val}"
            
            if encode in seen and encode not in self.taken:
                self.count.append(node)
                self.taken.add(encode)
            seen.add(encode)
            return encode
        
        dfs(root, set())
        return self.count