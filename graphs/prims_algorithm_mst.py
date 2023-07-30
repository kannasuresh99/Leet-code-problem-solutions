#User function Template for python3
from heapq import heapify, heappop, heappush

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        minHeap = []
        heapify(minHeap)
        
        heappush(minHeap, [0 ,0, -1])
        
        mst_sum = 0
        visited = set()
        
        while minHeap:
            wt, node, parent = heappop(minHeap)
            
            if node not in visited:
                mst_sum += wt
                for adj_node, adj_node_wt in adj[node]:
                    heappush(minHeap, [adj_node_wt, adj_node, node])
                    
            visited.add(node)
            
        return mst_sum

