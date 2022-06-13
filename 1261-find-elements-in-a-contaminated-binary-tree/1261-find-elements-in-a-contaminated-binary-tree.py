# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.nums = set()
        queue = deque()
        queue.append((root, 0))
        
        while queue:
            n = len(queue)
            for _ in range(n):
                node, val = queue.popleft()
                self.nums.add(val)
                if node.left:
                    queue.append((node.left, 2 * val + 1))
                if node.right:
                    queue.append((node.right, 2 * val + 2))
        
        
    def find(self, target: int) -> bool:
        return target in self.nums


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)