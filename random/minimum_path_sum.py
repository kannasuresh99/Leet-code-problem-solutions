#my solution
class Solution:
    def minPathSum(self, grid) -> int:
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if i == 0:
                    if j != 0:
                        grid[i][j] += grid[i][j-1]
                else:
                    if j == 0:
                        grid[i][j] += grid[i-1][j]
                    else:
                        right_sum = grid[i][j]+grid[i][j-1]
                        bottom_sum = grid[i][j]+grid[i-1][j]
                        grid[i][j] = min(right_sum,bottom_sum)
        print(grid)
        return grid[-1][-1]

res = Solution()
result = res.minPathSum([[1,2,3],[4,5,6]])
print(result)