"""
Algorithm Used: kadane's Algorithm
question link: https://leetcode.com/problems/maximum-subarray/
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        largest_sum = nums[0]

        for i in range(1, len(nums)):
            if curr_sum + nums[i] > nums[i]:
                curr_sum += nums[i]
            else:
                curr_sum = nums[i]
            largest_sum = max(largest_sum, curr_sum)
        
        return largest_sum

