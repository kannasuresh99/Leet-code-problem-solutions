# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0

    def getDiameter(self, node):
        if node is None:
            return 0
        
        left_height = self.getDiameter(node.left)
        right_height = self.getDiameter(node.right)

        self.diameter = max(self.diameter, left_height+right_height)

        return 1 + max(left_height, right_height)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.getDiameter(root)
        return self.diameter