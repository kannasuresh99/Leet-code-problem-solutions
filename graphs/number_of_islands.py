from collections import deque
from typing import List

class Solution:
    def bfs(self, row, col, grid, visited):
        visited.add(tuple([row, col]))
        queue = deque()
        queue.append([row, col])
        boundaries = [[-1,0],[1,0],[0,-1],[0,1]]
        while queue:
            row_, col_ = queue.popleft()
            for delrow, delcol in boundaries:
                nrow = row_ + delrow
                ncol = col_ + delcol
                if nrow < len(grid) and ncol < len(grid[0]) and nrow >= 0 and ncol >=0 and tuple([nrow, ncol]) not in visited and grid[nrow][ncol] == "1":
                    queue.append([nrow, ncol])
                    visited.add(tuple([nrow, ncol]))


    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        num_of_islands = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and tuple([row, col]) not in visited:
                    self.bfs(row, col, grid, visited)
                    num_of_islands += 1
        
        return num_of_islands