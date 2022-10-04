# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        
        
        def dfs(node, currSum):
            if not node:
                return 0
            
            currSum += node.val
            
            old = currSum - targetSum
            
            ans = prefixSum[old]
            
            prefixSum[currSum] += 1
            
            ans += dfs(node.left, currSum) + dfs(node.right, currSum)
            
            prefixSum[currSum] -= 1

            return ans
        
        return dfs(root, 0)
                
                
                
        