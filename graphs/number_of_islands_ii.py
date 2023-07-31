#User function Template for python3

from typing import List

class DisJointSet:
    def __init__(self, n):
        self.rank = [0 for _ in range(n+1)]
        self.size = [0 for _ in range(n+1)]
        self.parent = [i for i in range(n+1)]
        
    def findUltimateParent(self, node):
        #path compression
        if node == self.parent[node]:
            return node
        ulp = self.findUltimateParent(self.parent[node])
        self.parent[node] = ulp
        return self.parent[node]

    def unionByRank(self, u, v):
        up_u = self.findUltimateParent(u)
        up_v = self.findUltimateParent(v)
        
        if up_u == up_v:
            return
        
        if self.rank[up_u] < self.rank[up_v]:
            self.parent[up_u] = up_v
        elif self.rank[up_v] < self.rank[up_u]:
            self.parent[up_v] = up_u
        else:
            self.parent[u] = up_v
            self.rank[up_v] += 1
    
    def unionBySize(self, u, v):
        up_u = self.findUltimateParent(u)
        up_v = self.findUltimateParent(v)
        
        if up_u == up_v:
            return
        
        if self.size[up_u] < self.size[up_v]:
            self.parent[up_u] = up_v
            self.size[up_v] += self.size[up_u]
        else:
            self.parent[up_v] = up_u
            self.size[up_u] += self.size[up_v]
            

class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        # code here
        n = rows
        m = cols
        ds = DisJointSet(n*m)

        island = [[0]*m for _ in range(n)]

        count = 0
        result = []

        for operator in operators:
            row, col = operator
            #for duplicate operators handling
            if island[row][col] == 1:
                result.append(count)
                continue
            
            #setting island count to 1
            island[row][col] = 1
            count += 1
            boundaries = [[-1,0],[0,1],[0,-1],[1,0]]
            for delrow, delcol in boundaries:
                nrow = row + delrow
                ncol = col + delcol
                if nrow < n and ncol < m and nrow >= 0 and ncol >= 0 and island[nrow][ncol] == 1:
                    u = row*m + col
                    v = nrow*m + ncol
                    if ds.findUltimateParent(u) != ds.findUltimateParent(v):
                        ds.unionBySize(u, v)
                        count -= 1
            result.append(count)

        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3


    
if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        n = int(input())
        m = int(input())
        k = int(input())
        operators = []
        for i in range(k):
            u, v = map(int, input().strip().split())
            operators.append([u, v])
        obj = Solution()
        ans = obj.numOfIslands(n, m, operators)
        for i in ans:
            print(i, end = ' ')
        print()
            

# } Driver Code Ends