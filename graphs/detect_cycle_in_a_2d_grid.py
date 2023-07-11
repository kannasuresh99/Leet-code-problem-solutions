from typing import List


class Solution:
    def dfs(self, row, col, parent, grid, visited):
        visited.add(tuple([row, col]))

        boundaries = [[-1,0], [0,1], [0,-1], [1,0]]

        for delrow, delcol in boundaries:
            nrow = row + delrow
            ncol = col + delcol

            if nrow < len(grid) and ncol < len(grid[0]) and nrow >= 0 and ncol >= 0 and grid[nrow][ncol] == grid[row][col]:
                if tuple([nrow, ncol]) not in visited:
                    if self.dfs(nrow, ncol, [row, col], grid, visited):
                        return True
                elif tuple([nrow, ncol]) in visited and [nrow, ncol] != parent:
                    return True
        return False

    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = set()

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if tuple([i, j]) not in visited:
                    if self.dfs(i, j, [-1, -1], grid, visited):
                        print(visited)
                        return True
        
        return False