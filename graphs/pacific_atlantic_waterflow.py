from collections import deque
from typing import List

class Solution:
    def bfs(self, heights, queue, visited):
        boundaries = [[-1,0], [0,1],[1,0],[0,-1]]

        while queue:
            row, col = queue.popleft()
            for delrow, delcol in boundaries:
                nrow = row + delrow
                ncol = col + delcol
                if nrow < len(heights) and ncol < len(heights[0]) and nrow >= 0 and ncol >= 0 and visited[nrow][ncol] == False:
                    if heights[nrow][ncol] >= heights[row][col]:
                        visited[nrow][ncol] = True
                        queue.append([nrow, ncol])


    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        ROWS, COLS = len(heights), len(heights[0])

        pacific_visited = [[False]*COLS for _ in range(ROWS)]
        atlantic_visited = [[False]*COLS for _ in range(ROWS)]

        pacific_queue = deque()
        atlantic_queue = deque()

        #adding border rows to respective queues:
        for col in range(COLS):
            pacific_queue.append([0, col])
            atlantic_queue.append([ROWS-1, col])
            pacific_visited[0][col] = True
            atlantic_visited[ROWS-1][col] = True

        #adding border cols to respective queues:
        for row in range(ROWS):
            pacific_queue.append([row, 0])
            atlantic_queue.append([row, COLS-1])
            pacific_visited[row][0] = True
            atlantic_visited[row][COLS-1] = True

        self.bfs(heights, pacific_queue, pacific_visited)
        self.bfs(heights, atlantic_queue, atlantic_visited)

        #if the cells of both the visited array are matching then the water flows to both the oceans
        for i in range(ROWS):
            for j in range(COLS):
                if pacific_visited[i][j] and atlantic_visited[i][j]:
                    result.append([i,j])

        return result
        
