from collections import deque

class Solution:
    def nearest(self, grid):
        visited = set()
        queue = deque()
        result = []
        
        for i in range(0, len(grid)):
            result.append([])
            for j in range(0, len(grid[0])):
                result[i].append(0)
                if grid[i][j] == 1:
                    queue.append([[i, j], 0])
                    visited.add(tuple([i, j]))

        
        while queue:
            elem = queue.popleft()
            row, col = elem[0]
            nearest_dist = elem[1]
            
            result[row][col] = nearest_dist
            #print(row, col, result)
            
            boundaries = [[-1,0], [0,1], [0, -1], [1, 0]]
            
            for delrow, delcol in boundaries:
                nrow = row + delrow
                ncol = col + delcol
                
                if nrow < len(grid) and ncol < len(grid[0]) and nrow >= 0 and ncol >= 0 and tuple([nrow, ncol]) not in visited and grid[nrow][ncol] == 0:
                    queue.append([[nrow, ncol], nearest_dist+1])
                    visited.add(tuple([nrow, ncol]))
                    
        return result
    
sol = Solution()
res = sol.nearest([[0,1,1,0],[1,1,0,0],[0,0,1,1]])
print(res)