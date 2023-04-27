# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def helper(node, path_sum_arr, path_sum):
            nonlocal result
            if node is None:
                return

            left = helper(node.left, path_sum_arr+[node.val], path_sum+node.val)
            right = helper(node.right, path_sum_arr+[node.val], path_sum+node.val)

            if left is None and right is None:
                path_sum_arr.append(node.val)
                path_sum += node.val
                if path_sum == targetSum:
                    result.append(path_sum_arr)

            return path_sum
        
        helper(root, [], 0)
        return result