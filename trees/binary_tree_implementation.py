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

    def levelOrderTraversal(self, root):
        queue = [root]
        result = list()

        while queue != []:
            next_queue = list()
            current_level_result = list()
            for root in queue:
                current_level_result.append(root.data)
                if root.left:
                    next_queue.append(root.left)
                if root.right:
                    next_queue.append(root.right)
                
            queue = next_queue
            result.append(current_level_result)
        print(result)
        return result

    def inOrderIterativeTraversal(self, root):
        stack = []
        result = []
        curr_node = root

        while curr_node or stack != []:
            while curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            curr_node = stack.pop()
            result.append(curr_node.data)
            curr_node = curr_node.right

        print(result)
        return result

    def preOrderIterativeTraversal(self, root):
        stack = [root]
        result = []

        while stack != []:
            curr = stack.pop()
            result.append(curr.data)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        print(result)
        return result



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
print()
print("-------------------------------")
print()
print("Levelorder Traversal")
root.levelOrderTraversal(root)
print()
print("-------------------------------")
print()
print("Inorder Iterative Traversal")
root.inOrderIterativeTraversal(root)
print()
print("-------------------------------")
print()
print("Preorder Iterative Traversal")
root.preOrderIterativeTraversal(root)