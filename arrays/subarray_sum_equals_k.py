"""
question link: https://leetcode.com/problems/subarray-sum-equals-k/
"""

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_sum_dict = {0: 1}
        prefix_sum = 0

        for i in range(0, len(nums)):
            prefix_sum += nums[i]
            res += prefix_sum_dict.get(prefix_sum - k, 0)
            prefix_sum_dict[prefix_sum] = prefix_sum_dict.get(prefix_sum, 0)+1
        
        return res

