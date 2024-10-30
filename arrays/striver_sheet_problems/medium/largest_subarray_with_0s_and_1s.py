class Solution:
    def maxLen(self,arr, N):
        # code here
        for i in range(N):
            if arr[i] == 0:
                arr[i] = -1
        
        prefix_sum = 0
        prefix_hashmap = {}
        max_len = 0
        
        for i in range(N):
            prefix_sum += arr[i]
            if prefix_sum == 0:
                max_len = max(max_len, i+1)
            elif prefix_sum in prefix_hashmap:
                max_len = max(max_len, i-prefix_hashmap[prefix_sum])
            
            if prefix_sum not in prefix_hashmap:
                prefix_hashmap[prefix_sum] = i
        
        return max_len

