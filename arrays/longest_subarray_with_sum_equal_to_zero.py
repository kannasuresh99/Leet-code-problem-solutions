#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        """
        if subarray from i to j equals to S
        then for a array with negative elements
        subarray from x to j equals to 0
        so subarray, arr[i:x]+arr[x:j] = S + 0 = S
        
        Using the above algorithm we solve this problem
        """
        max_len = 0
        
        prefix_sum_index_dict = {}
        
        prefix_sum = 0
        
        for i in range(n):
            prefix_sum += arr[i]
            if prefix_sum == 0:
                max_len = i+1
            else:
                if prefix_sum in prefix_sum_index_dict:
                    max_len = max(max_len, i-prefix_sum_index_dict[prefix_sum])
                else:
                    prefix_sum_index_dict[prefix_sum] = i
        
        return max_len

