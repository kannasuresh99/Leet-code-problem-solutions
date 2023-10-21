"""question link: https://leetcode.com/problems/set-matrix-zeroes/"""

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])

        is_row_zero = [False for _ in range(ROWS)]
        is_col_zero = [False for _ in range(COLS)]

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    is_row_zero[i] = True
                    is_col_zero[j] = True
        
        for row in range(ROWS):
            if is_row_zero[row]:
                for col in range(COLS):
                    matrix[row][col] = 0
        
        for col in range(COLS):
            if is_col_zero[col]:
                for row in range(ROWS):
                    matrix[row][col] = 0
        