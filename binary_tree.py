class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("Kannappan")
newBT.leftChild = TreeNode("Doss")
newBT.rightChild = TreeNode("Ramalingam")
newBT.leftChild.leftChild = TreeNode("Anandh")
newBT.leftChild.rightChild = TreeNode("Thilaga")
newBT.rightChild.leftChild = TreeNode("Suresh")
newBT.rightChild.rightChild = TreeNode("Prabha")

#time complexity O(N)
#space complexity O(N) due to stack memory usage
def preOrderTraversal(rootNode):
    if not rootNode:
        return []
    return [rootNode.data] + preOrderTraversal(rootNode.leftChild) + preOrderTraversal(rootNode.rightChild) #time complexity O(N/2)

#time complexity O(N)
#space complexity O(N) due to stack memory usage
def inOrderTraversal(rootNode):
    if not rootNode:
        return []
    return inOrderTraversal(rootNode.leftChild) + [rootNode.data] + inOrderTraversal(rootNode.rightChild)

"""
inOrderTraversal(Doss) + [kannappan] + inOrderTraversal(Ramalingam)
[Anandh, Doss, Thilaga] + [kannappan] + [Suresh, Ramalingam, Prabha]
[Anandh, Doss, Thilaga, Kannappan, Suresh, Ramalingam, Prabha]

    inOrderTraversal(Doss)
    inOrderTraversal(Anandh) + [Doss] + inOrderTraversal(Thilaga)
    [Anandh] + [Doss] + [Thilaga]
    [Anandh, Doss, Thilaga]

        inOrderTraversal(Anandh)
        inOrderTraversal(None) + [Anandh] + inOrderTraversal(None)
        [] + [Anandh] + []
        [Anandh]

        inOrderTraversal(Thilaga)
        inOrderTraversal(None) + [Thilaga] + inOrderTraversal(None)
        [] + [Thilaga] + []
        [Thilaga]

    inOrderTraversal(Ramalingam)
    inOrderTraversal(Suresh) + [Ramalingam] + inOrderTraversal(Prabha)
    [Suresh] + [Ramalingam] + [Prabha]
    [Suresh, Ramalingam, Prabha]

        inOrderTraversal(Suresh)
        inOrderTraversal(None) + [Suresh] + inOrderTraversal(None)
        [] + [Suresh] + []
        [Suresh]

        inOrderTraversal(Prabha)
        inOrderTraversal(None) + [Prabha] + inOrderTraversal(None)
        [] + [Prabha] + []
        [Prabha]
"""

def postOrderTraversal(rootnode):
    if rootnode is None:
        return []
    return postOrderTraversal(rootnode.rightChild) + postOrderTraversal(rootnode.leftChild) + [rootnode.data]

def levelOrderTraversal(rootnode):
    if rootnode is None:
        return []
    queue = [rootnode]
    result = []

    while queue != []:
        next_queue = []
        nodes = []
        for root in queue:
            nodes.append(root.data)
            if root.leftChild:
                next_queue.append(root.leftChild)
            if root.rightChild:
                next_queue.append(root.rightChild)
        result.append(nodes)
        queue = next_queue
    return result


print("preOrderTraversal:", preOrderTraversal(newBT))
print("inOrderTraversal:",inOrderTraversal(newBT))
print("postOrderTraversal:",postOrderTraversal(newBT))
print("levelOrderTraversal:",levelOrderTraversal(newBT))