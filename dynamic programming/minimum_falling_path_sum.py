from typing import List

#recursive solution
class Solution:
    def recurse(self, row, col, n, m, matrix):
        if row == 0:
            return matrix[0][col]
        
        sum_up = float('inf')
        sum_left_diagonal = float('inf')
        sum_right_diagonal = float('inf')

        nrow_up = row - 1
        ncol_left = col - 1
        ncol_right = col + 1

        if nrow_up >= 0:
            sum_up = matrix[row][col] + self.recurse(nrow_up, col, n, m, matrix)
            if ncol_left >= 0:
                sum_left_diagonal = matrix[row][col] + self.recurse(nrow_up, ncol_left, n, m, matrix)
            if ncol_right < m:
                sum_right_diagonal = matrix[row][col] + self.recurse(nrow_up, ncol_right, n, m, matrix)
        
        return min(sum_up, sum_left_diagonal, sum_right_diagonal)

    
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        min_sum = float('inf')
        for j in range(m):
            min_sum = min(min_sum, self.recurse(n-1, j, n, m, matrix))
        return min_sum
    
#memoization solution
class Solution:
    def recurse(self, row, col, n, m, matrix, dp):
        if row == 0:
            return matrix[0][col]
        
        if dp[row][col]:
            return dp[row][col]

        nrow_up = row - 1
        ncol_left = col - 1
        ncol_right = col + 1

        sum_up = float('inf')
        sum_left_diagonal = float('inf')
        sum_right_diagonal = float('inf')

        if nrow_up >= 0:
            sum_up = matrix[row][col] + self.recurse(nrow_up, col, n, m, matrix, dp)
            if ncol_left >= 0:
                sum_left_diagonal = matrix[row][col] + self.recurse(nrow_up, ncol_left, n, m, matrix, dp)
            if ncol_right < m:
                sum_right_diagonal = matrix[row][col] + self.recurse(nrow_up, ncol_right, n, m, matrix, dp)
        
        dp[row][col] = min(sum_up, sum_left_diagonal, sum_right_diagonal)
        
        return dp[row][col]

    
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        min_sum = float('inf')
        dp = [[None]*m for _ in range(n)]
        for j in range(m):
            min_sum = min(min_sum, self.recurse(n-1, j, n, m, matrix, dp))
        return min_sum
    
#tabulation solution
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[None]*m for _ in range(n)]

        #setting base cases
        for j in range(m):
            dp[0][j] = matrix[0][j]
        
        
        #core logic
        for row in range(1, n):
            for col in range(m):
                nrow_up = row - 1
                ncol_left = col - 1
                ncol_right = col + 1

                sum_up = float('inf')
                sum_left_diagonal = float('inf')
                sum_right_diagonal = float('inf')

                if nrow_up >= 0:
                    sum_up = matrix[row][col] + dp[nrow_up][col]
                    if ncol_left >= 0:
                        sum_left_diagonal = matrix[row][col] + dp[nrow_up][ncol_left]
                    if ncol_right < m:
                        sum_right_diagonal = matrix[row][col] + dp[nrow_up][ncol_right]
                
                dp[row][col] = min(sum_up, sum_left_diagonal, sum_right_diagonal)
        
        #since we need to find minimum path sum of elements in the last row we do this
        return min(dp[n-1])
    
    
