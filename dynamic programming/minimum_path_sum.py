from typing import List

#recursive solution
class Solution:
    def recurse(self, row, col, n, m, grid):
        if row == 0 and col == 0:
            return grid[0][0]
        
        nrow = row - 1
        ncol = col - 1
        sum_up = float('inf')
        sum_left = float('inf')

        if nrow >= 0:
            sum_up = grid[row][col] + self.recurse(nrow, col, n, m, grid)
        if ncol >= 0:
            sum_left = grid[row][col] + self.recurse(row, ncol, n, m, grid)
        
        return min(sum_up, sum_left)


    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        return self.recurse(n-1, m-1, n, m, grid)
    
#memoization solution
class Solution:
    def recurse(self, row, col, n, m, grid, dp):
        if row == 0 and col == 0:
            return grid[0][0]
        
        if dp[row][col]:
            return dp[row][col]
        
        nrow = row - 1
        ncol = col - 1
        sum_up = float('inf')
        sum_left = float('inf')

        if nrow >= 0:
            sum_up = grid[row][col] + self.recurse(nrow, col, n, m, grid, dp)
        if ncol >= 0:
            sum_left = grid[row][col] + self.recurse(row, ncol, n, m, grid, dp)
        
        dp[row][col] = min(sum_up, sum_left)
        
        return dp[row][col]


    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[None]*m for _ in range(n)]
        return self.recurse(n-1, m-1, n, m, grid, dp)

#tabulation solution
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[None]*m for _ in range(n)]
        dp[0][0] = grid[0][0]

        for row in range(n):
            for col in range(m):
                if row == 0 and col == 0:
                    continue
                
                nrow = row - 1
                ncol = col - 1
                sum_up = float('inf')
                sum_left = float('inf')

                if nrow >= 0:
                    sum_up = grid[row][col] + dp[nrow][col]
                if ncol >= 0:
                    sum_left = grid[row][col] + dp[row][ncol]
                
                dp[row][col] = min(sum_up, sum_left)

        return dp[n-1][m-1]

