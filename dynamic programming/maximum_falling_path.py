#User function Template for python3

class Solution:
    def maximumPath(self, N, Matrix):
        # code here
        dp = [[None]*N for _ in range(N)]
        
        #setting base cases
        for j in range(N):
            dp[0][j] = Matrix[0][j]
        
        
        #core logic
        for row in range(1, N):
            for col in range(N):
                nrow_up = row - 1
                ncol_left = col - 1
                ncol_right = col + 1

                sum_up = float('-inf')
                sum_left_diagonal = float('-inf')
                sum_right_diagonal = float('-inf')

                if nrow_up >= 0:
                    sum_up = Matrix[row][col] + dp[nrow_up][col]
                    if ncol_left >= 0:
                        sum_left_diagonal = Matrix[row][col] + dp[nrow_up][ncol_left]
                    if ncol_right < N:
                        sum_right_diagonal = Matrix[row][col] + dp[nrow_up][ncol_right]
                
                dp[row][col] = max(sum_up, sum_left_diagonal, sum_right_diagonal)

        return max(dp[N-1])


