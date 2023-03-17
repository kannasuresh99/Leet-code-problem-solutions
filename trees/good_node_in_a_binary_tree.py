class Solution:
    def __init__(self):
        self.good_nodes = 0

    def helper(self, node, curr_max):
        if node is None:
            return 

        if node.val >= curr_max:
            self.good_nodes += 1
            curr_max = node.val
        
        self.helper(node.left, curr_max)
        self.helper(node.right, curr_max)

        return

    def goodNodes(self, root: TreeNode) -> int:
        self.helper(root, root.val)
        return self.good_nodes