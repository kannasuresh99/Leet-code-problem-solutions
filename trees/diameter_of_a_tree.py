# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_max_depth_of_a_node(self, node, depth):
        if node is None:
            return depth
        left_depth = self.get_max_depth_of_a_node(node.left, depth+1)
        right_depth = self.get_max_depth_of_a_node(node.right, depth+1)
        return max(left_depth, right_depth)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        left_max_depth = self.get_max_depth_of_a_node(root.left, 0)
        right_max_depth = self.get_max_depth_of_a_node(root.right, 0)
        return left_max_depth+right_max_depth