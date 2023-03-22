# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_path = float('-inf')

    def get_max_gain(self, node):
        if node is None:
            return 0
                
        gain_on_left = max(self.get_max_gain(node.left), 0)
        gain_on_right = max(self.get_max_gain(node.right), 0)
        current_max_path = node.val + gain_on_left + gain_on_right
        self.max_path = max(self.max_path, current_max_path)
        return node.val + max(gain_on_left, gain_on_right)

    def maxPathSum(self, root: TreeNode) -> int:
        self.get_max_gain(root)
        return self.max_path