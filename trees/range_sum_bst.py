class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        return self.helper(root, low, high, 0)

    def helper(self, node, low, high, result):
        if node is None:
            return result
        if node.val >= low and node.val <= high:
            result += node.val
        result = self.helper(node.left, low, high, result)
        result = self.helper(node.right, low, high, result)
        return result