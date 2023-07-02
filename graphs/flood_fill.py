from collections import deque
from typing import List

#BFS solution
class Solution:
    def bfs(self, image, row, col, visited, color):
        visited.add(tuple([row, col]))
        ref_color = image[row][col]
        image[row][col] = color
        queue = deque()
        queue.append([row, col])
        boundaries = [[-1,0],[1,0],[0,1],[0,-1]]

        while queue:
            row_, col_ = queue.popleft()
            for delrow, delcol in boundaries:
                nrow = row_ + delrow
                ncol = col_ + delcol
                if nrow < len(image) and ncol < len(image[0]) and nrow >= 0 and ncol >= 0 and image[nrow][ncol] == ref_color and tuple([nrow, ncol]) not in visited:
                    image[nrow][ncol] = color
                    visited.add(tuple([nrow, ncol]))
                    queue.append([nrow, ncol])
        return image 


    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        return self.bfs(image, sr, sc, visited, color)
    
#DFS solution
class Solution:
    def dfs(self, image, row, col, visited, color, ref_color):
        visited.add(tuple([row, col]))
        image[row][col] = color
        boundaries = [[-1,0],[1,0],[0,1],[0,-1]]

        for delrow, delcol in boundaries:
            nrow = row + delrow
            ncol = col + delcol
            if nrow < len(image) and ncol < len(image[0]) and nrow >= 0 and ncol >= 0 and image[nrow][ncol] == ref_color and tuple([nrow, ncol]) not in visited:
                self.dfs(image, nrow, ncol, visited, color, ref_color)
        return image 


    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        ref_color = image[sr][sc]
        return self.dfs(image, sr, sc, visited, color, ref_color)
