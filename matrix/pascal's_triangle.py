"""question link: https://leetcode.com/problems/pascals-triangle/"""

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1],[1,1]]

        for row in range(2, numRows+1):
            curr_row = [1]*(row+1)
            for i in range(1, row):
                curr_row[i] = res[row-1][i-1] + res[row-1][i]
            res.append(curr_row)
        
        return res[:numRows]
        