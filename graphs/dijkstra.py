from heapq import heapify, heappop, heappush

class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        minHeap = []
        heapify(minHeap)
        heappush(minHeap, [0, S])
        
        dist = [float('inf') for _ in range(V)]
        #dont always assume 0 as source, check if there is source given in the question
        dist[S] = 0
        
        
        while minHeap:
            wt, node = heappop(minHeap)
            
            for adj_node, adj_node_wt in adj[node]:
                if dist[node] + adj_node_wt < dist[adj_node]:
                    dist[adj_node] = dist[node] + adj_node_wt
                    heappush(minHeap, [dist[adj_node], adj_node])
                    
        return dist
    
