#User function Template for python3

from typing import List
from collections import deque
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        if start == end:
            return 0
        queue = deque()
        queue.append([0, start])
        
        dist = [float('inf') for _ in range(100000)]
        dist[start] = 0
        
        while queue:
            steps, node = queue.popleft()
            
            for num in arr:
                new_num = (num*node)%100000
                if steps + 1 < dist[new_num]:
                    dist[new_num] = steps + 1
                    if new_num == end:
                        return dist[new_num]
                    queue.append([dist[new_num], new_num])
                    
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends