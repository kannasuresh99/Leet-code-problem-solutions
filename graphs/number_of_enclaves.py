from typing import List
from collections import deque

#DFS solution
class Solution:
    def dfs(self, grid, row, col, visited):
        visited.add(tuple([row, col]))

        boundaries = [[-1,0], [0,1], [0, -1], [1, 0]]

        for delrow, delcol in boundaries:
            nrow = row + delrow
            ncol = col + delcol

            if nrow < len(grid) and ncol < len(grid[0]) and nrow >= 0 and ncol >= 0 and tuple([nrow, ncol]) not in visited and grid[nrow][ncol] == 1:
                self.dfs(grid, nrow, ncol, visited)
                visited.add(tuple([nrow, ncol]))
        

    def numEnclaves(self, grid: List[List[int]]) -> int:
        visited = set()
        number_of_enclaves = 0

        for col in range(0, len(grid[0])):
            #traverse 1st row
            if grid[0][col] == 1:
                self.dfs(grid, 0, col, visited)
            
            #traverse last row
            if grid[len(grid)-1][col] == 1:
                self.dfs(grid, len(grid)-1, col, visited)

        for row in range(0, len(grid)):
            #traverse 1st col
            if grid[row][0] == 1:
                self.dfs(grid, row, 0, visited)

            #traverse last col
            if grid[row][len(grid[0])-1] == 1:
                self.dfs(grid, row, len(grid[0])-1, visited)

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1 and tuple([i, j]) not in visited:
                    number_of_enclaves += 1


        return number_of_enclaves
    

#BFS solution

class Solution:
    def bfs(self, grid, queue, visited):
        while queue:
            row, col = queue.popleft()

            boundaries = [[-1,0], [0,1], [0, -1], [1, 0]]

            for delrow, delcol in boundaries:
                nrow = row + delrow
                ncol = col + delcol

                if nrow < len(grid) and ncol < len(grid[0]) and nrow >= 0 and ncol >= 0 and tuple([nrow, ncol]) not in visited and grid[nrow][ncol] == 1:
                    visited.add(tuple([nrow, ncol]))
                    queue.append([nrow, ncol])
        

    def numEnclaves(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        number_of_enclaves = 0

        for col in range(0, len(grid[0])):
            #traverse 1st row
            if grid[0][col] == 1:
                queue.append([0, col])
                visited.add(tuple([0, col]))
            
            #traverse last row
            if grid[len(grid)-1][col] == 1:
                queue.append([len(grid)-1, col])
                visited.add(tuple([len(grid)-1, col]))

        for row in range(0, len(grid)):
            #traverse 1st col
            if grid[row][0] == 1:
                queue.append([row, 0])
                visited.add(tuple([row, 0]))

            #traverse last col
            if grid[row][len(grid[0])-1] == 1:
                queue.append([row, len(grid[0])-1])
                visited.add(tuple([row, len(grid[0])-1]))
        
        self.bfs(grid, queue, visited)

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1 and tuple([i, j]) not in visited:
                    number_of_enclaves += 1


        return number_of_enclaves
        