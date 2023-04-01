# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, str_num):
            if node is None:
                return

            num = str_num + str(node.val)
            left_num = dfs(node.left, num)
            right_num = dfs(node.right, num)

            if not left_num and not right_num:
                self.sum += int(num, 2)
            return num
        dfs(root, "")
        return self.sum
        
