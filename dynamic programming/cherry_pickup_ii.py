from typing import List

#recursive solution
class Solution:
    def recurse(self, row, col1, col2, n, m, grid):
        if col1 < 0 or col2 < 0 or col1 >= m or col2 >= m:
            return -1e8
    
        if row == n-1:
            #for common destination
            if col1 == col2:
                return grid[row][col1]
            #for different destination
            else:
                return grid[row][col1] + grid[row][col2]
        
        max_sum = -1e8
        for delcol1 in range(-1, 2):
            for delcol2 in range(-1, 2):
                nrow = row + 1
                ncol1 = col1 + delcol1
                ncol2 = col2 + delcol2

                value = 0
                if col1 == col2:
                    value = grid[row][col1]
                else:
                    value = grid[row][col1] + grid[row][col2]
                value += self.recurse(nrow, ncol1, ncol2, n, m, grid)
                max_sum = max(max_sum, value)
        
        return max_sum


    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        return self.recurse(0, 0, m-1, n, m, grid)
    
#memoization solution
class Solution:
    def recurse(self, row, col1, col2, n, m, grid, dp):
        if col1 < 0 or col2 < 0 or col1 >= m or col2 >= m:
            return -1e8
    
        if row == n-1:
            #for common destination
            if col1 == col2:
                return grid[row][col1]
            #for different destination
            else:
                return grid[row][col1] + grid[row][col2]
        
        if dp[row][col1][col2]:
            return dp[row][col1][col2]
        
        max_sum = -1e8
        for delcol1 in range(-1, 2):
            for delcol2 in range(-1, 2):
                nrow = row + 1
                ncol1 = col1 + delcol1
                ncol2 = col2 + delcol2

                value = 0
                if col1 == col2:
                    value = grid[row][col1]
                else:
                    value = grid[row][col1] + grid[row][col2]
                value += self.recurse(nrow, ncol1, ncol2, n, m, grid, dp)
                max_sum = max(max_sum, value)
        dp[row][col1][col2] = max_sum
        
        return dp[row][col1][col2]


    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[[None]*m for _ in range(m)] for _ in range(n)]
        return self.recurse(0, 0, m-1, n, m, grid, dp)

#tabulation
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[[None]*m for _ in range(m)] for _ in range(n)]
        
        #setting base cases
        for col1 in range(m):
            for col2 in range(m):
                if col1 == col2:
                    dp[n-1][col1][col2] = grid[n-1][col1]
                else:
                    dp[n-1][col1][col2] = grid[n-1][col1] + grid[n-1][col2]

        for row in range(n-2, -1, -1):
            for col1 in range(m):
                for col2 in range(m):
                    max_sum = -1e8
                    for delcol1 in range(-1, 2):
                        for delcol2 in range(-1, 2):
                            nrow = row + 1
                            ncol1 = col1 + delcol1
                            ncol2 = col2 + delcol2

                            value = -1e8
                            if col1 == col2:
                                value = grid[row][col1]
                            else:
                                value = grid[row][col1] + grid[row][col2]
                            if ncol1 >= 0 and ncol2 >= 0 and ncol1 < m and ncol2 < m:
                                value += dp[nrow][ncol1][ncol2]
                            max_sum = max(max_sum, value)
                    dp[row][col1][col2] = max_sum
        
        return dp[0][0][m-1]
