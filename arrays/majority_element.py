"""
Algorithm Used: Moore's Voting Algorithm
question link: https://leetcode.com/problems/majority-element/
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #using Moore's Voting algorithm
        majority_element = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == majority_element:
                count += 1
            else:
                count -= 1
                if count == 0:
                    majority_element = nums[i]
                    count = 1
        
        return majority_element

