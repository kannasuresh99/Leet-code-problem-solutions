# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.is_binary_tree_balanced = True

    def helper(self, node):
        if node is None:
            return 0
        
        left_height = self.helper(node.left)
        right_height = self.helper(node.right)

        if abs(left_height-right_height) > 1:
            self.is_binary_tree_balanced = False

        return 1 + max(left_height, right_height)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.helper(root)
        return self.is_binary_tree_balanced