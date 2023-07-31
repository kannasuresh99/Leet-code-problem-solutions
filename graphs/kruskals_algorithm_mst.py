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
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        mst_sum = 0
        edges = []
        
        for i in range(V):
            for adj_node, wt in adj[i]:
                edges.append([wt, [i, adj_node]])
        
        #important step
        edges.sort(key=lambda x:x[0])
        
        ds = DisJointSet(V)
        for edge in edges:
            wt = edge[0]
            u, v = edge[1]
            
            if ds.findUltimateParent(u) != ds.findUltimateParent(v):
                mst_sum += wt
                ds.unionBySize(u, v)
            
        return mst_sum
                
