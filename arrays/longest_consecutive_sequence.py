"""
question link: https://leetcode.com/problems/longest-consecutive-sequence/
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = 1
        nums_set = set(nums)

        for i in range(0, len(nums)):
            if nums[i]-1 not in nums_set:
                cnt = 1
                curr_num = nums[i]
                while curr_num+1 in nums_set:
                    curr_num += 1
                    cnt += 1
                res = max(res, cnt)
        
        return res

