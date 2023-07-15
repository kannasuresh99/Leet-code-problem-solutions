#User function Template for python3
from collections import deque
import string

class Solution:
    def findOrder(self,alien_dict, N, K):
        adjList = [[] for _ in range(K)]
        queue = deque()
        result = []

        #core logic
        for i in range(0, len(alien_dict)-1):
            str1 = alien_dict[i]
            str2 = alien_dict[i+1]
            
            len_ = min(len(str1), len(str2))
            
            for j in range(0, len_):
                if str1[j] != str2[j]:
                    adjList[ord(str1[j])-ord('a')].append(ord(str2[j])-ord('a'))
                    break
        
        #topo sort template
        indegree = [0 for d in range(K)]
        
        for k in range(K):
            for adj_node in adjList[k]:
                indegree[adj_node] += 1
                
        
        for l in range(0, len(indegree)):
            if indegree[l] == 0:
                queue.append(l)
                
        
        while queue:
            node_ = queue.popleft()
            result.append(node_)
            
            for adj_node in adjList[node_]:
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    queue.append(adj_node)
                    
        for idx, num in enumerate(result):
            result[idx] = string.ascii_lowercase[num]
            
        return result

