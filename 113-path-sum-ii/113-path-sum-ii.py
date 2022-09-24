# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        
        def backtracking(node, collected, collectedSum):
            nonlocal targetSum
    
            if not node:
                return
            
            collectedSum += node.val
            collected.append(node.val)

            if not node.left and not node.right:
                if collectedSum == targetSum:
                    ans.append(collected[::])
                    collected.pop()
                    return

            
            backtracking(node.right, collected, collectedSum)
            backtracking(node.left, collected, collectedSum)
            
            popped = collected.pop()

        backtracking(root, [], 0)
        
        return ans
            
            
        