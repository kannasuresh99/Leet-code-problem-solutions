#User function Template for python3

from typing import List
from collections import deque

class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        # code here
        visited = set()
        queue = deque()
        queue.append([0, source])
        visited.add(tuple(source))
        
        while queue:
            dist, coordinates = queue.popleft()
            row, col = coordinates

            if coordinates == destination:
                return dist
            
            boundaries = [[-1, 0], [0, 1], [0, -1], [1, 0]]
            
            for delrow, delcol in boundaries:
                nrow = row + delrow
                ncol = col + delcol
                if nrow < len(grid) and ncol < len(grid[0]) and nrow >= 0 and ncol >= 0 and tuple([nrow, ncol]) not in visited and grid[nrow][ncol] == 1:
                    queue.append([dist+1, [nrow, ncol]])
                    visited.add(tuple([nrow, ncol]))
                    
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

         
if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        source = [0] * 2
        source[0], source[1] = map(int,input().strip().split())
        destination = [0] * 2
        destination[0], destination[1] = map(int,input().strip().split())
        obj=Solution()
        print(obj.shortestPath(grid, source, destination))
# } Driver Code Ends