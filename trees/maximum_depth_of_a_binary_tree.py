# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_depth = float('-inf')

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def helper(node, depth):
            if node is None:
                return

            left = helper(node.left, depth+1)
            right = helper(node.right, depth+1)

            if left is None and right is None:
                if depth > self.max_depth:
                    self.max_depth = depth

            return depth

        helper(root, 1)
        return self.max_depth