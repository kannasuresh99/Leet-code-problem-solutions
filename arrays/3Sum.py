"""
question link: https://leetcode.com/problems/3sum/
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #solving using sorting and two-pointer approach
        nums.sort()
        result = []
        
        for i in range(0, len(nums)):
            #to avoid duplicate triplets
            if i>0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                sum_ = nums[i] + nums[j] + nums[k]
                if sum_ < 0:
                    j += 1
                elif sum_ > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        
        return result

