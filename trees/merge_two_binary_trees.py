# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root1, root2):
            if root1 is None and root2 is None:
                return None

            root1_left = None
            root2_left = None
            root1_right = None
            root2_right = None

            if root1 is None:
                root_val = root2.val
                root2_left = root2.left
                root2_right = root2.right
            elif root2 is None:
                root_val = root1.val
                root1_left = root1.left
                root1_right = root1.right
            else:
                root_val = root1.val + root2.val
                root1_left = root1.left
                root1_right = root1.right
                root2_left = root2.left
                root2_right = root2.right
            
            root = TreeNode(root_val)
            root.left = dfs(root1_left, root2_left)
            root.right = dfs(root1_right, root2_right)
            return root
        return dfs(root1, root2)
         