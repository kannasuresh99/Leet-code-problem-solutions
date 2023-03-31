# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.val] + self.inorder(node.right)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        inorder_arr = self.inorder(root)
        new_tree = TreeNode(inorder_arr[0])
        curr = new_tree

        for i in range(1, len(inorder_arr)):
            curr.right = TreeNode(inorder_arr[i])
            curr = curr.right
        return new_tree


