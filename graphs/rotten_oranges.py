from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        max_time = 0
        visited = set()
        queue = deque()
        boundaries = [[-1,0],[0, 1],[1,0],[0, -1]]
        ROWS, COLS = len(grid), len(grid[0])

        for i in range(0, ROWS):
            for j in range(0, COLS):
                if grid[i][j] == 2:
                    queue.append([[i,j], 0])
                    visited.add(tuple([i, j]))
                elif grid[i][j] == 0:
                    visited.add(tuple([i, j]))


        while queue:
            elem = queue.popleft()
            row, col = elem[0]
            time = elem[1]
            max_time = max(max_time, time)

            for delrow, delcol in boundaries:
                nrow = row + delrow
                ncol = col + delcol

                if nrow < ROWS and ncol < COLS and nrow >= 0 and ncol >= 0 and grid[nrow][ncol] == 1 and tuple([nrow, ncol]) not in visited:
                    visited.add(tuple([nrow, ncol]))
                    grid[nrow][ncol] = 2
                    queue.append([[nrow, ncol], time+1])

        if len(visited) != ROWS*COLS:
            return -1
        
        return max_time

