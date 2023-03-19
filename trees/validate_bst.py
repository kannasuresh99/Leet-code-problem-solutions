# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validate(self, node, left, right):
        if node is None:
            return True
        
        if not (node.val > left and node.val < right):
            return False

        return self.validate(node.left, left, node.val) and self.validate(node.right, node.val, right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float('-inf'), float('inf'))