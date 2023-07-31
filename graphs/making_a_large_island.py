from typing import List

class DisJointSet:
    def __init__(self, n):
        self.rank = [0 for _ in range(n+1)]
        self.size = [1 for _ in range(n+1)]
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
    def largestIsland(self, grid: List[List[int]]) -> int:
        #create a disjointset
        n = len(grid)
        ds = DisJointSet(n*n)

        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    continue
                boundaries = [[-1,0],[0,1],[0,-1],[1,0]]
                for delrow, delcol in boundaries:
                    nrow = row + delrow
                    ncol = col + delcol
                    if nrow < n and ncol < n and nrow >= 0 and ncol >= 0 and grid[nrow][ncol] == 1:
                        u = row*n + col
                        v = nrow*n + ncol
                        ds.unionBySize(u, v)

        max_area = 0
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    boundaries = [[-1,0],[0,1],[0,-1],[1,0]]
                    components = set()
                    sumTotal = 1 #taking the 0 itself as a part of island
                    for delrow, delcol in boundaries:
                        nrow = row + delrow
                        ncol = col + delcol
                        if nrow < n and ncol < n and nrow >= 0 and ncol >= 0 and grid[nrow][ncol] == 1:
                            v = nrow*n + ncol
                            components.add(ds.findUltimateParent(v))
                    
                    for val in components:
                        sumTotal += ds.size[val]
                    
                    max_area = max(max_area, sumTotal)

        for cell in range(n*n):
            max_area = max(max_area, ds.size[ds.findUltimateParent(cell)])
        
        return max_area



