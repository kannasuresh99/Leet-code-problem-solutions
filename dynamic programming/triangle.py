from typing import List

#memoization solution
class Solution:
    def recurse(self, row, col, triangle, dp):
        if row == len(triangle)-1:
            return triangle[row][col]
        
        if dp[row][col]:
            return dp[row][col]

        nrow = row + 1
        ncol = col + 1

        sum_same_index = triangle[row][col] + self.recurse(nrow, col, triangle, dp)
        sum_next_index = triangle[row][col] + self.recurse(nrow, ncol, triangle, dp)
        dp[row][col] = min(sum_same_index, sum_next_index)
        return dp[row][col]


    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[None]*len(triangle[i]) for i in range(len(triangle))]
        return self.recurse(0, 0, triangle, dp)
    

#tabulation solution
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[None]*len(triangle[i]) for i in range(len(triangle))]
        dp[len(triangle)-1] = triangle[len(triangle)-1]

        for row in range(len(triangle)-2, -1, -1):
            for col in range(len(triangle[row])):
                nrow = row + 1
                ncol = col + 1
                sum_same_index = triangle[row][col] + dp[nrow][col]
                sum_next_index = triangle[row][col] + dp[nrow][ncol]
                dp[row][col] = min(sum_same_index, sum_next_index)

        return dp[0][0]