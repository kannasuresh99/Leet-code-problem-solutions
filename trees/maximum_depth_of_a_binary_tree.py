# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, length):
        if node is None:
            return length
        left_length = self.helper(node.left, length+1)
        right_length = self.helper(node.right, length+1)
        return max(left_length, right_length)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)