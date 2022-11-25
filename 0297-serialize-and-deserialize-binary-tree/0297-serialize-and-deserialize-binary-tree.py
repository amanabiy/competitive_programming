# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        queue = deque([root])
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    ans.append('@')
                else:
                    ans.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
    
        ans = '#'.join(ans)
        return ans
        
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """        
        nodes = []
        data = data.split('#')
        parent = 0
        child = 2
        
        for i in range(len(data)):
            if data[i] != '@':
                nodes.append(TreeNode(int(data[i])))
            else:
                nodes.append(None)
        
        for i in range(len(data)):
            if data[i] != '@':
                nodes[i].left = nodes[child - 1]
                nodes[i].right = nodes[child]
                child += 2
        
        return nodes[0]
                
        
        
        
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))