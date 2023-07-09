import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def dfs(self, row, col, grid, visited, island_arr, base_row, base_col):
        visited.add(tuple([row, col]))
        island_arr.append([row-base_row, col-base_col])
        
        boundaries = [[-1,0], [0,1], [0,-1], [1,0]]
        
        for delrow, delcol in boundaries:
            nrow = row + delrow
            ncol = col + delcol
            
            if nrow < len(grid) and ncol < len(grid[0]) and nrow >= 0 and ncol >= 0 and tuple([nrow, ncol]) not in visited and grid[nrow][ncol] == 1:
                visited.add(tuple([nrow, ncol]))
                self.dfs(nrow, ncol, grid, visited, island_arr, base_row, base_col)
    

    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        visited = set()
        island_set = list()
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if tuple([i,j]) not in visited and grid[i][j] == 1:
                    island_arr = list()
                    self.dfs(i, j, grid, visited, island_arr, i, j)
                    if island_arr not in island_set:
                        island_set.append(island_arr)
                    
        
        return len(island_set)

