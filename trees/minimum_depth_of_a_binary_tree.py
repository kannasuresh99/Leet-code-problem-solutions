# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.min_path = float('inf')

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        def helper(node, depth):
            if node is None:
                return

            left = helper(node.left, depth+1)
            right = helper(node.right, depth+1)

            if left is None and right is None:
                if depth < self.min_path:
                    self.min_path = depth
            
            return depth
        helper(root, 1)
        return self.min_path