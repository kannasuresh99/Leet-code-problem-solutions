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
        
    
    def isBelongToSameComponent(self, u, v):
        if self.findUltimateParent(u) == self.findUltimateParent(v):
            print("Same")
            return
        else:
            print("Not Same")
            return
            
ds = DisJointSet(7)
# ds.unionByRank(1,2)
# ds.unionByRank(2,3)
# ds.unionByRank(4,5)
# ds.unionByRank(6,7)
# ds.unionByRank(5,6)

# ds.isBelongToSameComponent(3, 7)

# ds.unionByRank(3, 7)

# ds.isBelongToSameComponent(3, 7)

# print(ds.rank)

# print()

ds.unionBySize(1,2)
ds.unionBySize(2,3)
ds.unionBySize(4,5)
ds.unionBySize(6,7)
ds.unionBySize(5,6)

ds.isBelongToSameComponent(3, 7)

ds.unionBySize(3, 7)

ds.isBelongToSameComponent(3, 7)

print(ds.size)