"""
question link: https://leetcode.com/problems/4sum/
"""

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #solving this in same way as 3Sum
        #time complexity O(N**3)
        res = []
        nums.sort()

        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j+1
                l = len(nums)-1
                while k < l:
                    sum_ = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum_ < target:
                        k += 1
                    elif sum_ > target:
                        l -= 1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
        return res

