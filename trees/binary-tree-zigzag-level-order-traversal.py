# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        ans = []
        queue = [root]
        count = 0
        while queue:
            next_queue = []
            level_ans = []
            for i in range(0, len(queue)):
                level_ans.append(queue[i].val)
                if queue[i].left:
                    next_queue.append(queue[i].left)
                if queue[i].right:
                    next_queue.append(queue[i].right)
            
            if count % 2 == 1:
                level_ans.reverse()
            count += 1
            ans.append(level_ans)
            queue = next_queue
        return ans