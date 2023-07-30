from collections import defaultdict
from typing import List


class Solution:
    def dfs(self, node, visited, adjList):
        visited.add(node)
        for node_ in adjList[node]:
            if node_ not in visited:
                self.dfs(node_, visited, adjList)
        return

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        adjList = defaultdict(list)
        num_of_provinces = 0

        for i in range(0, len(isConnected)):
            for j in range(0, len(isConnected[i])):
                if isConnected[i][j] != 0:
                    adjList[i].append(j)
        
        for i in range(len(isConnected)):
            if i not in visited:
                self.dfs(i, visited, adjList)
                num_of_provinces += 1
        
        return num_of_provinces
    
#disjoint solution
#User function Template for python3
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
    def numProvinces(self, adj, V):
        # code here 
        ds = DisJointSet(V)
        number_of_provinces = 0
        
        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1:
                    ds.unionBySize(i ,j)
                    
        for k in range(V):
            if ds.parent[k] == k:
                number_of_provinces += 1
                
        return number_of_provinces
