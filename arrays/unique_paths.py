"""
Additional Topic: Dynamic Programming
Question Link: https://leetcode.com/problems/unique-paths/
"""

class Solution:
    def recurse(self, row, col, m, n, dp):
        if row == 0 and col == 0:
            return 1
        
        if dp[row][col]:
            return dp[row][col]

        nrow = row - 1
        ncol = col - 1
        paths_left = 0
        paths_up = 0

        if ncol >= 0:
            paths_left = self.recurse(row, ncol, m, n, dp)
        if nrow >= 0:
            paths_up = self.recurse(nrow, col, m, n, dp)
        
        dp[row][col] = paths_left + paths_up

        return dp[row][col]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None]*n for _ in range(m)]
        return self.recurse(m-1, n-1, m, n, dp)


