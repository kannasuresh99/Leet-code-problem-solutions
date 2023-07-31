from typing import List

class DisJoinSet:
    def __init__(self, n):
        self.size = [1 for _ in range(n+1)]
        self.parent = [i for i in range(n+1)]

    def find_ultimate_parent(self, node):
        if node == self.parent[node]:
            return node
        
        self.parent.extend
        
        ultimate_parent = self.find_ultimate_parent(self.parent[node])
        self.parent[node] = ultimate_parent
        return self.parent[node]

    def union_by_size(self, u, v):
        ulp_u = self.find_ultimate_parent(u)
        ulp_v = self.find_ultimate_parent(v)

        if ulp_u == ulp_v:
            return
        
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        extra_edges = 0
        num_of_components = 0
        
        ds = DisJoinSet(n)

        for edge in connections:
            u, v = edge
            if ds.find_ultimate_parent(u) != ds.find_ultimate_parent(v):
                ds.union_by_size(u, v)
            else:
                extra_edges += 1
        
        for i in range(n):
            if i == ds.parent[i]:
                num_of_components += 1
        
        #minimum number of edges to connect components = number of components - 1
        if extra_edges >= num_of_components-1:
            return num_of_components-1
        return -1
    

