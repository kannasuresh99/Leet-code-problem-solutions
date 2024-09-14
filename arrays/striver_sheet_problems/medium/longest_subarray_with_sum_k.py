"""
longest subarray with sum k with negative numbers
"""

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        prefix_sum = 0
        prefix_sum_hashmap = {}
        max_len = 0
        
        for i in range(0, n):
            prefix_sum += arr[i]
            if prefix_sum == k:
                max_len = max(max_len, i+1)
            elif prefix_sum-k in prefix_sum_hashmap:
                max_len = max(max_len, i-prefix_sum_hashmap[prefix_sum-k])
            if prefix_sum not in prefix_sum_hashmap:
                prefix_sum_hashmap[prefix_sum] = i
        return max_len

res = Solution().lenOfLongSubarr([10, 5, 2, 7, 8, -9, -1, 0, 5, 0, 9, -8, 5, -2, 7, 6, 5, 3, 1], 19, 6)
print(res)