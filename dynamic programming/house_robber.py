from typing import List

class Solution:
    
    def recurse(self, idx, nums):
        if idx == 0:
            return nums[0]
        
        if idx <= 0:
            return 0
        
        pick = nums[idx] + self.recurse(idx-2, nums)
        not_pick = self.recurse(idx-1, nums)
        
        return max(pick, not_pick)
    
    def memoize(self, idx, nums, dp):
        if idx == 0:
            return nums[0]
        
        if idx < 0:
            return 0
        
        if dp[idx]:
            return dp[idx]
        
        pick = nums[idx] + self.recurse(idx-2, nums, dp)
        not_pick = self.recurse(idx-1, nums, dp)
        
        dp[idx] = max(pick, not_pick)
        
        return dp[idx]
    
    def rob_with_recursion(self, nums: List[int]) -> int:
        n = len(nums)
        return self.recurse(n-1, nums)
        
    def rob_with_memoization(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [None for _ in range(n)]
        return self.memoize(n-1, nums, dp)
        
    def rob_with_tabulation(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [None for _ in range(n)]
        dp[0] = nums[0]
        
        for i in range(1, n):
            pick = nums[i]
            if i > 1:
                pick += dp[i-2]
            not_pick = dp[i-1]
            
            dp[i] = max(pick, not_pick)
            
        return dp[n-1]
    
    def rob_with_space_optimization(self, nums: List[int]) -> int:
        n = len(nums)
        prev2 = nums[0]
        prev = nums[0]

        for i in range(1, n):
            pick = nums[i]
            if i > 1:
                pick += prev2
            not_pick = prev
            curr = max(pick, not_pick)
            prev2 = prev
            prev = curr

        return prev