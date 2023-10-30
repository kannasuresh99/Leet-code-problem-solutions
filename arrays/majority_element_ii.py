"""
Algorithm Used: Moore's Voting Algorithm
question link: https://leetcode.com/problems/majority-element-ii/
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #altering Moore's voting algorithm to solve this problem
        res = []

        elem1 = float('-inf')
        elem2 = float('-inf')
        count1 = 0
        count2 = 0

        n = len(nums)

        for i in range(n):
            if count1 == 0 and nums[i] != elem2:
                elem1 = nums[i]
                count1 = 1
            elif count2 == 0 and nums[i] != elem1:
                elem2 = nums[i]
                count2 = 1
            elif nums[i] == elem1:
                count1 += 1
            elif nums[i] == elem2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1 = 0
        count2 = 0

        for i in range(n):
            if nums[i] == elem1:
                count1 += 1
            if nums[i] == elem2:
                count2 += 1
        
        if count1 > (n//3):
            res.append(elem1)
        if count2 > (n//3):
            res.append(elem2)

        res.sort()

        return res

