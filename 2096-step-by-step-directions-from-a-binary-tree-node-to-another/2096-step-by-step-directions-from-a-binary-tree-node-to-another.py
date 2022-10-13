# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], val1: int, val2: int) -> str:

        def lowestCommonAncestor(node, cand1, cand2):
            if not node:
                return None

            left = lowestCommonAncestor(node.left, cand1, cand2)
            right = lowestCommonAncestor(node.right, cand1, cand2)

            if left and right:
                return node

            if node.val == cand1 or node.val == cand2:
                return node

            return left or right


        def findDepthSrc(node, src, depth):
            if not node:
                return 0

            if src == node.val:
                return depth

            left = findDepthSrc(node.left, src, depth + 1)
            right = findDepthSrc(node.right, src, depth + 1)

            return max(left, right)

        def goDown(node, dst):
            if not node:
                return []
            if node.val == dst:
                return ["."]

            left = goDown(node.left, dst)
            right = goDown(node.right, dst)

            if right:
                right.append('R')
                return right
            if left:
                left.append('L')
                return left

            return []

        # def pathBetweenNodes(root, val1, val2):
        commonAncestor = lowestCommonAncestor(root, val1, val2)
        ans = ""
        # handle if common Ancestor == val2 which is the destination
        if commonAncestor.val != val1:
            ans = "U" * findDepthSrc(commonAncestor, val1, 0)
        down = ''.join(reversed(goDown(commonAncestor, val2)[1:]))
        return ans + down

