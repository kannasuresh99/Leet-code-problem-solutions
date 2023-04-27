# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.is_path = False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return 0

        def helper(node, sum_):
            if node is None:
                return

            left = helper(node.left, sum_+node.val)
            right = helper(node.right, sum_+node.val)

            if left is None and right is None:
                sum_ += node.val
                if sum_ == targetSum:
                    self.is_path = True

            return sum_
        
        helper(root, 0)
        return self.is_path

            