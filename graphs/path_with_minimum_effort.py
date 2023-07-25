from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        minHeap = []
        heapify(minHeap)
        heappush(minHeap, [0, [0, 0]])
        diff = []
        for i in range(len(heights)):
            arr = []
            for j in range(len(heights[0])):
                arr.append(float('inf'))
            diff.append(arr)

        while minHeap:
            curr_max_diff, coordinates = heappop(minHeap)
            row, col = coordinates

            if coordinates == [len(heights)-1, len(heights[0])-1]:
                return curr_max_diff

            boundaries = [[-1,0], [0,1], [1, 0], [0,-1]]

            for delrow, delcol in boundaries:
                nrow = row + delrow
                ncol = col + delcol

                if nrow < len(heights) and ncol < len(heights[0]) and nrow >= 0 and ncol >= 0:
                    newEffort = max(curr_max_diff, abs(heights[row][col] - heights[nrow][ncol]))
                    if newEffort < diff[nrow][ncol]:
                        diff[nrow][ncol] = newEffort
                        heappush(minHeap, [newEffort, [nrow, ncol]])

        return 0