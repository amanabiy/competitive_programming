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
        if data[0] == '@':
            return None
        
        nodes = [TreeNode()]
        data = data.split('#')
        parent = 0
        child = 2
        
        for _ in range(1, len(data)):
            nodes.append(None)
        
        for i in range(len(data)):
            if data[i] != '@':
                nodes[i].val = int(data[i])
                leftChild = child - 1
                rightChild = child
                if leftChild < len(data) and data[leftChild] != '@':
                    nodes[leftChild] = TreeNode()
                    nodes[i].left = nodes[leftChild]
                if rightChild < len(data) and data[rightChild] != '@':
                    nodes[rightChild] = TreeNode()
                    nodes[i].right = nodes[rightChild]
                child += 2
        
        return nodes[0]
                
        
        
        
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))