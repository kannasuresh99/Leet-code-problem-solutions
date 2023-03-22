from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        output =[]
        def check(root):
            if not root:
                output.append("#")
            if root:
                output.append(str(root.val))
                check(root.left)
                check(root.right)
        check(root)
        return ','.join(output)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        node_list = data.split(",")
        node_list = deque(node_list)
        
        def create():
            if node_list:
                value = node_list.popleft()
                if(value == "#"):
                    return None
                else:
                    node = TreeNode(int(value))
                    node.left= create()
                    node.right = create()
                return node
        
        home = create()
        return home