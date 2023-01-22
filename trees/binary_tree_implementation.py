class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def inOrderTraversal(self, root):
        if root is None:
            return
        self.inOrderTraversal(root.left)
        print(root.data)
        self.inOrderTraversal(root.right)
        return

    def preOrderTraversal(self, root):
        if root is None:
            return

        print(root.data)
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)
        return

    def postOrderTraversal(self, root):
        if root is None:
            return

        self.postOrderTraversal(root.left)
        self.postOrderTraversal(root.right)
        print(root.data)
        return

root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(13)
root.insert(14)
print("Inorder Traversal:")
root.inOrderTraversal(root)
print()
print("-------------------------------")
print()
print("Preorder Traversal")
root.preOrderTraversal(root)
print()
print("-------------------------------")
print()
print("Postorder Traversal")
root.postOrderTraversal(root)