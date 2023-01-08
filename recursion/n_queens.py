class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        board_rows_list = [["."]*n for r_ in range(n)]
        visited_left = set()
        visited_inc_row_dec_col_diagonals = set() #sum
        visited_inc_row_inc_col_diagonals = set() #diff

        def NQueens(row):
            if row == n:
                result.append(["".join(row) for row in board_rows_list])
                return

            for col in range(0, n):
                sum_ = row + col
                diff_ = row - col
                if not (col in visited_left or sum_ in visited_inc_row_dec_col_diagonals or diff_ in visited_inc_row_inc_col_diagonals):
                    visited_left.add(col)
                    visited_inc_row_dec_col_diagonals.add(sum_)
                    visited_inc_row_inc_col_diagonals.add(diff_)
                    board_rows_list[row][col] = "Q"
                    NQueens(row+1)
                    visited_left.remove(col)
                    visited_inc_row_dec_col_diagonals.remove(sum_)
                    visited_inc_row_inc_col_diagonals.remove(diff_)
                    board_rows_list[row][col] = "."
            return
        NQueens(0)
        return result
            
res = Solution().solveNQueens(n=4)
print(res)