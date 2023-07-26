#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def relax_edges(self, edges, dist, is_nth_relaxation=None):
        for edge in edges:
            u = edge[0]
            v = edge[1]
            wt = edge[2]
            if dist[u] != int(1e8) and dist[u] + wt < dist[v]:
                if is_nth_relaxation:
                    return True
                dist[v] = dist[u] + wt
        
        return False

    def bellman_ford(self, V, edges, S):
        #code here
        dist = [int(1e8) for _ in range(V)]
        dist[S] = 0
        
        for i in range(V-1):
            self.relax_edges(edges, dist)
        
        #This checks if the values are getting reduced even after n-1 iterations
        #which in turn means that there is an negative cycle
        if self.relax_edges(edges, dist, is_nth_relaxation=True):
            return [-1]
            
        return dist
        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        edges = []
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            edges.append([u,v,w])
        S=int(input())
        ob = Solution()
        
        res = ob.bellman_ford(V,edges,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends