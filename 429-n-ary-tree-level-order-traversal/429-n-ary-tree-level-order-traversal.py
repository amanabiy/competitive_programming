"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        queue = deque([root])
        ans = []
        
        while queue:
            ans.append([i.val for i in queue])
            for i in range(len(queue)):
                node = queue.popleft()
                for neigh in node.children:
                    queue.append(neigh)
        
        return ans
        