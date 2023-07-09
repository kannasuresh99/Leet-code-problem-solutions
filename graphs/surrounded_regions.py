from typing import List

class Solution:
    def dfs(self, board, row, col, visited):
        visited.add(tuple([row, col]))

        boundaries = [[-1,0], [0, 1], [1, 0], [0, -1]]

        for delrow, delcol in boundaries:
            nrow = row + delrow
            ncol = col + delcol

            if nrow < len(board) and ncol < len(board[0]) and nrow >= 0 and ncol >= 0 and tuple([nrow, ncol]) not in visited and board[nrow][ncol] == "O":
                self.dfs(board, nrow, ncol, visited)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()

        for col in range(0, len(board[0])):
            #traverse first row
            if board[0][col] == "O":
                self.dfs(board, 0, col, visited)
            
            #traverse last row
            if board[len(board)-1][col] == "O":
                self.dfs(board, len(board)-1, col, visited)

        for row in range(0, len(board)):
            #traverse first col
            if board[row][0] == "O":
                self.dfs(board, row, 0, visited)
            
            #traverse last row
            if board[row][len(board[0])-1] == "O":
                self.dfs(board, row, len(board[0])-1, visited)

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == "O" and tuple([i, j]) not in visited:
                    board[i][j] = "X"
