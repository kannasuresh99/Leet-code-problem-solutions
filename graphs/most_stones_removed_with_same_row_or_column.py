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
    def removeStones(self, stones: List[List[int]]) -> int:
        """
        Number of stones removed = total no of stones - no of components
        """
        total_no_of_stones = len(stones)
        max_row = 0
        max_col = 0

        for row, col in stones:
            max_row = max(max_row, row)
            max_col = max(max_col, col)

        ds = DisJointSet(max_row+max_col+1)

        stone_nodes = dict()
        for stone in stones:
            u = stone[0]
            #main logic to find column in disjoint set
            v = stone[1] + max_row + 1
            ds.unionBySize(u, v)
            stone_nodes[u] = 1
            stone_nodes[v] = 1
        
        no_of_connected_components = 0
        for key in stone_nodes:
            if ds.findUltimateParent(key) == key:
                no_of_connected_components += 1
        
        result = total_no_of_stones - no_of_connected_components

        return result

