"""
Solved using Kadane's Algorithm

Explanation of Kadane's Algorithm:
    - We can solve this problem using Kadane's Algorithm
    - We can iterate through the array and maintain two variables max_sum and current_sum
    - If the current_sum is less than 0, we can update the current_sum to 0
    - If the current_sum is greater than the max_sum, we can update the max_sum to the current_sum
    - Finally, we can return the max_sum
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        curr_sum = 0

        for i in range(0, len(nums)):
            if curr_sum + nums[i] > nums[i]:
                curr_sum += nums[i]
            else:
                curr_sum = nums[i]
            max_sum = max(max_sum, curr_sum)
        return max_sum
    
res = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(res)
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6
