#basic tree
class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children
    
    def __str__(self, level=0):
        ret = "  " * level + str(self.data)  + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addChild(self, child):
        self.children.append(child)

tree = TreeNode('Kannappan', [])
ramalingam = TreeNode('Ramalingam', [])
doss = TreeNode('Doss', [])
tree.addChild(ramalingam)
tree.addChild(doss)
suresh = TreeNode('sureshkannan', [])
prabha = TreeNode('prabha', [])
anand = TreeNode('anand', [])
thilaga = TreeNode('thilaga', [])
divya = TreeNode('divya', [])
viji = TreeNode('viji', [])
ramalingam.addChild(suresh)
ramalingam.addChild(prabha)
doss.addChild(anand)
doss.addChild(thilaga)
doss.addChild(divya)
doss.addChild(viji)
kannappan = TreeNode('kannappan', [])
jayalakshmi = TreeNode('jayalakshmi', [])
suresh.addChild(jayalakshmi)
suresh.addChild(kannappan)
print(tree)