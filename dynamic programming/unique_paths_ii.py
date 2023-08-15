from typing import List

#memoization solution
class Solution:
    def recurse(self, row, col, n, m, grid, dp):
        if row == 0 and col == 0:
            if grid[row][col] == 1:
                return 0
            return 1
        
        if grid[row][col] == 1:
            return 0
        
        if dp[row][col]:
            return dp[row][col]

        nrow = row - 1
        ncol = col - 1
        paths_up = 0
        paths_left = 0

        if nrow >= 0:
            paths_up = self.recurse(nrow, col, n, m, grid, dp)
        if ncol >= 0:
            paths_left = self.recurse(row, ncol, n, m, grid, dp)
        
        dp[row][col] = paths_up + paths_left
        
        return dp[row][col]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[None]*m for _ in range(n)]
        return self.recurse(n-1, m-1, n, m, obstacleGrid, dp)

#tabulation solution
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[None]*m for _ in range(n)]

        dp[0][0] = 1
        if obstacleGrid[0][0] == 1:
            dp[0][0] = 0
        
        if obstacleGrid[n-1][m-1] == 1:
            return 0

        for row in range(n):
            for col in range(m):
                if row == 0 and col == 0:
                    continue
                
                nrow = row - 1
                ncol = col - 1
                paths_up = 0
                paths_left = 0

                if nrow >= 0 and obstacleGrid[nrow][col] != 1:
                    paths_up = dp[nrow][col]
                if ncol >= 0 and obstacleGrid[row][ncol] != 1:
                    paths_left = dp[row][ncol]
                
                dp[row][col] = paths_left + paths_up
        
        return dp[n-1][m-1]