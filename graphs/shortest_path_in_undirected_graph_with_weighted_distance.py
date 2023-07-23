#User function Template for python3
from heapq import heapify, heappop, heappush

class Solution:
    def shortestPath(self, n, m, edges):
        # Code here
        shortest_path = []
        adjList = [[] for _ in range(n+1)]
        for edge in edges:
            u = edge[0]
            v = edge[1]
            wt = edge[2]
            adjList[u].append([v, wt])
            adjList[v].append([u, wt])
            
        dist = [float('inf') for d in range(n+1)]
        dist[1] = 0
        
        parent = [p for p in range(n+1)]
        
        minHeap = []
        heapify(minHeap)
        heappush(minHeap, [0, 1])
        
        while minHeap:
            wt, node = heappop(minHeap)
            
            for adj_node, edg_wt in adjList[node]:
                if wt + edg_wt < dist[adj_node]:
                    dist[adj_node] = wt + edg_wt
                    parent[adj_node] = node
                    heappush(minHeap, [dist[adj_node], adj_node])
        
        node = n
        #memoization technique to find shortest path from parents
        while parent[node] != node:
            shortest_path.append(node)
            node = parent[node]
        shortest_path.append(1)
        shortest_path.reverse()
        
        return shortest_path if dist[n] != float('inf') else [-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        edges = []
        for i in range(m):
            node1, node2, weight = list(map(int, input().split()))
            edges.append([node1, node2, weight])
        obj = Solution()
        ans = obj.shortestPath(n, m, edges)
        for e in ans:
            print(e, end = ' ')
        print()
# } Driver Code Ends