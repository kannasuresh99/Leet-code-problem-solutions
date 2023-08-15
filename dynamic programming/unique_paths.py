#recursive solution
class Solution:
    def recurse(self, row, col, m, n):
        if row == 0 and col == 0:
            return 1

        nrow = row - 1
        ncol = col - 1
        paths_left = 0
        paths_up = 0

        if ncol >= 0:
            paths_left = self.recurse(row, ncol, m, n)
        if nrow >= 0:
            paths_up = self.recurse(nrow, col, m, n)
        
        return paths_left + paths_up

    def uniquePaths(self, m: int, n: int) -> int:
        return self.recurse(m-1, n-1, m, n)

#memoization solution
class Solution:
    def recurse(self, row, col, m, n, dp):
        if row == 0 and col == 0:
            return 1

        if dp[row][col]:
            return dp[row][col]

        nrow = row - 1
        ncol = col - 1
        paths_right = 0
        paths_down = 0

        if ncol >= 0:
            paths_right = self.recurse(row, ncol, m, n, dp)
        if nrow >= 0:
            paths_down = self.recurse(nrow, col, m, n, dp)
        
        dp[row][col] = paths_right + paths_down
        
        return dp[row][col]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None]*n for _ in range(m)]
        return self.recurse(m-1, n-1, m, n, dp)


#tabulation solution
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None]*n for _ in range(m)]
        dp[0][0] = 1
        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    continue
                
                nrow = row - 1
                ncol = col - 1
                paths_up = 0
                paths_left = 0

                if ncol >= 0:
                    paths_left = dp[row][ncol]
                if nrow >= 0:
                    paths_up = dp[nrow][col]
                
                dp[row][col] = paths_left + paths_up

        return dp[m-1][n-1]
    
