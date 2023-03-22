# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
    def __init__(self):
        self.s = []

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def serialize_helper(node):
            if node is None:
                self.s.append('N')
                return
            
            self.s.append(str(node.val))
            serialize_helper(node.left)
            serialize_helper(node.right)
        serialize_helper(root)
        return ",".join(self.s)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        p = data.split(',')
        q = deque(p)

        def deserialize_helper():
            if q:
                node_val = q.popleft()
                if node_val == 'N':
                    return None
                
                root = TreeNode(node_val)
                root.left = deserialize_helper()
                root.right = deserialize_helper()
                return root
        return deserialize_helper()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))