#User function Template for python3

class Solution:
    
    def sort_nodes(self, node, adj, sort_visited, stack):
        sort_visited.add(node)
        
        for adj_node in adj[node]:
            if adj_node not in sort_visited:
                self.sort_nodes(adj_node, adj, sort_visited, stack)
                
        stack.append(node)
    
    def dfs(self, node, adj, count_visited):
        count_visited.add(node)
        
        for adj_node in adj[node]:
            if adj_node not in count_visited:
                self.dfs(adj_node, adj, count_visited)
        
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # code here
        """
        Kosaraju algorithm:
            1. sort the nodes based on the finishing time by storing it in a stack
            2. reverse the edges
            3. count the strongly connected components
        """
        
        #step 1 - sorting nodes
        sort_visited = set()
        stack = []
        
        for i in range(V):
            if i not in sort_visited:
                self.sort_nodes(i, adj, sort_visited, stack)
        
        #step 2 - reversing edges
        adjRev = [[] for _ in range(V)]
        for i in range(V):
            for adj_node in adj[i]:
                adjRev[adj_node].append(i)
                
        #step 3 - count the number of strongly connected components
        count_visited = set()
        no_of_sc_components = 0
        while stack:
            i = stack.pop()
            if i not in count_visited:
                self.dfs(i, adjRev, count_visited)
                no_of_sc_components += 1
        
        return no_of_sc_components


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends