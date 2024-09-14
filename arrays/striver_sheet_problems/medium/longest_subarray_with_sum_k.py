"""
longest subarray with sum k with negative numbers

Thought process behind the solution:
    - If the length of a subarray is equal to x, and our target sum is k
    - If we have a prefix sum of y at index i, and we have a prefix sum of y-k at index j
    - Then the sum of the subarray from j+1 to i will be equal to k
    - We can use this property to solve this problem

Algorithm:
    - We can use prefix sum to solve this problem
    - We can use hashmap to store the prefix sum and the index at which it occured
    - We can iterate through the array and calculate the prefix sum
    - If the prefix sum is equal to k, we can update the max_len to max(max_len, i+1)
    - If the prefix sum-k is in the hashmap, we can update the max_len to max(max_len, i-prefix_sum_hashmap[prefix_sum-k])
    - If the prefix sum is not in the hashmap, we can add the prefix sum to the hashmap
    - Finally, we can return the max_len
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