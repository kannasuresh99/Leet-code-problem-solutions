from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        visited = set()
        visited.add(tuple([0, 0]))
        queue = deque()
        queue.append([1, [0, 0]])

        while queue:
            dist, coordinates = queue.popleft()
            row, col = coordinates

            if coordinates == [len(grid)-1, len(grid[0])-1]:
                return dist

            for delrow in range(-1, 2):
                for delcol in range(-1, 2):
                    nrow = row + delrow
                    ncol = col + delcol

                    if nrow < len(grid) and ncol < len(grid[0]) and nrow >= 0 and ncol >= 0 and tuple([nrow, ncol]) not in visited and grid[nrow][ncol] == 0:
                        queue.append([dist+1, [nrow, ncol]])
                        visited.add(tuple([nrow, ncol]))

        return -1
