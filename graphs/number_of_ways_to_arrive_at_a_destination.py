from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        #dijkstra implementation
        #create adjacency list
        mod = int(1e9 + 7)
        adjList = [[] for _ in range(n)]

        for edge in roads:
            u = edge[0]
            v = edge[1]
            wt = edge[2]
            adjList[u].append([v, wt])
            adjList[v].append([u, wt])

        minHeap = []
        heapify(minHeap)
        heappush(minHeap, [0, 0])

        dist = [float('inf') for d in range(n)]
        dist[0] = 0
        ways = [0 for w in range(n)]
        ways[0] = 1

        while minHeap:
            dis, node = heappop(minHeap)

            for adj_node, edgWt in adjList[node]:
                if dis + edgWt < dist[adj_node]:
                    dist[adj_node] = dis + edgWt
                    ways[adj_node] = ways[node]
                    heappush(minHeap ,[dist[adj_node], adj_node])
                elif dis + edgWt == dist[adj_node]:
                    ways[adj_node] += ways[node]

        return ways[n-1]%mod
