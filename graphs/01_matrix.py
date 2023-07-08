from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited = set()
        queue = deque()
        result = [[None]*len(row_) for row_ in mat]
        
        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                if mat[i][j] == 0:
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
                
                if nrow < len(mat) and ncol < len(mat[0]) and nrow >= 0 and ncol >= 0 and tuple([nrow, ncol]) not in visited:
                    queue.append([[nrow, ncol], nearest_dist+1])
                    visited.add(tuple([nrow, ncol]))
                    
        return result