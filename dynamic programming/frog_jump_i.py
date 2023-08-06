from typing import List

class Solution:

    def recurse_with_memoization(self, idx, heights, dp):
        if idx == 0:
            return 0
        
        if dp[idx]:
            return dp[idx]
        
        left = self.recurse_with_memoization(idx-1, heights, dp) + abs(heights[idx] - heights[idx-1])
        right = float('inf')
        if idx > 1:
            right = self.recurse_with_memoization(idx-2, heights, dp) + abs(heights[idx] - heights[idx-2])
        
        dp[idx] = min(left, right)
        return dp[idx]
    
    def recurse(self, idx, heights):
        if idx == 0:
            return 0
        
        left = self.recurse(idx-1, heights) + abs(heights[idx] - heights[idx-1])
        right = float('inf')
        if idx > 1:
            right = self.recurse(idx-2, heights) + abs(heights[idx] - heights[idx-2])
        
        return min(left, right)

    def frogJump(self, n: int, heights: List[int]) -> int:
        return self.recurse(n-1, heights)
    
    def frogJumpMemoization(self, n: int, heights: List[int]) -> int:
        dp = [None for _ in range(n)]
        return self.recurse_with_memoization(n-1, heights, dp)
    
    def frogJumpTabulation(self, n: int, heights: List[int]) -> int:
        dp = [None for _ in range(n)]
        dp[0] = 0
        
        for idx in range(1, n):
            left = dp[idx-1] + abs(heights[idx] - heights[idx-1])
            right = float('inf')
            if idx > 1:
                right = dp[idx-2] + abs(heights[idx] - heights[idx-2])
            
            dp[idx] = min(left, right)

        return dp[n-1]
    
    def frogJumpConstantSpace(self, n: int, heights: List[int]) -> int:
         # Write your code here
        prev = 0 #idx - 1 -> b
        prev2 = 0 #idx - 2 - > a
        
        for idx in range(1, n):
            left = prev + abs(heights[idx] - heights[idx-1])
            right = float('inf')
            if idx > 1:
                right = prev2 + abs(heights[idx] - heights[idx-2])
            
            curr = min(left, right)
            prev2 = prev
            prev = curr

        return prev




#recursion solution
print(Solution().frogJump(4, [10, 20, 30, 10]))

#memoization solution
print(Solution().frogJumpMemoization(4, [10, 20, 30, 10]))

#tabulation solution
print(Solution().frogJumpTabulation(4, [10, 20, 30, 10]))

#optimal solution with constant space
print(Solution().frogJumpConstantSpace(4, [10, 20, 30, 10]))