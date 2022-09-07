# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = deque()
        def dfs(node):
            if not node:
                return deque()
            left = dfs(node.left)
            right = dfs(node.right)
            
            
            if right:
                left.appendleft('(')
                left.append(')')
                right.appendleft('(')
                right.append(')')
                return deque(deque([str(node.val)]) + left + right)
            elif left:
                left.appendleft('(')
                left.append(')')
                return deque(deque([str(node.val)]) + left)
            else:
                return deque(deque([str(node.val)]))

        ans = dfs(root)

        return ''.join(ans)