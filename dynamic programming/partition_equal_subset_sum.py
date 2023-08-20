from typing import List

class Solution:
    def is_subset_sum_equals_to_k_exists(self, N, sum, arr):
        dp = [[False]*(sum+1) for _ in range(N)]
        
        # Setting base cases
        for i in range(N):
            dp[i][0] = True
            
        dp[0][0] = True
        if arr[0] <= sum:
            dp[0][arr[0]] = True
        
        # Core logic
        for idx in range(1, N):
            for target in range(1, sum+1):
                pick = False
                if target >= arr[idx]:
                    pick = dp[idx-1][target-arr[idx]]
                not_pick = dp[idx-1][target]
        
                dp[idx][target] = pick or not_pick
        return dp[N-1][sum]

    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        #we can't create two subsets of same sum, if the total sum is odd
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2

        return self.is_subset_sum_equals_to_k_exists(len(nums), target, nums)
