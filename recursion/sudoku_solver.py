class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValidEntry(board, char, row, col):
            for k in range(0,9):
                if board[row][k] == char:
                    return False
                if board[k][col] == char:
                    return False
                if board[3*(row//3)+k//3][3*(col//3)+k%3] == char:
                    return False
            return True

        def Solve(board):

            for row in range(0, 9):
                for col in range(0, 9):
                    if board[row][col] == ".":
                        for i in range(1, 10):
                            if isValidEntry(board, str(i), row, col):
                                board[row][col] = str(i)
                                if Solve(board):
                                    return True
                                else:
                                    board[row][col] = "."
                        return False
            return True

        Solve(board)

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
res = Solution().solveSudoku(board=board)
print(board)