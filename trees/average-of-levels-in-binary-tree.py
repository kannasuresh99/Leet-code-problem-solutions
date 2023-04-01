# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root]
        ans = []

        while queue != []:
            next_queue = []
            sum_ = 0
            for node in queue:
                sum_ += node.val
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            ans.append(sum_/len(queue))
            queue = next_queue
        return ans
            