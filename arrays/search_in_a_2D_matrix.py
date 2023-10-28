
"""question link: https://leetcode.com/problems/search-a-2d-matrix/"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = (m*n)-1

        while left <= right:
            mid = (left+right)//2
            #calculating row and col index based on total number of columns
            row = mid//n
            col = mid%n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid+1
            else:
                right = mid-1
        return False

