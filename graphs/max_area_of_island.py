from collections import deque
from typing import List

class Solution:
    def bfs(self, row, col, grid, visited):
        visited.add(tuple([row, col]))
        queue = deque()
        queue.append([row, col])
        
        island_count = 0

        while queue:
            row, col = queue.popleft()

            island_count += 1
            
            boundaries = [[-1,0], [0,1], [0,-1], [1,0]]

            for delrow, delcol in boundaries:
                nrow = row + delrow
                ncol = col + delcol

                if nrow < len(grid) and ncol < len(grid[0]) and nrow >= 0 and ncol >= 0 and tuple([nrow, ncol]) not in visited and grid[nrow][ncol] == 1:
                    queue.append([nrow, ncol])
                    visited.add(tuple([nrow, ncol]))

        return island_count


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if tuple([i,j]) not in visited and grid[i][j] == 1:
                    island_count = self.bfs(i, j, grid, visited)
                    islands = max(islands, island_count)

        return islands

