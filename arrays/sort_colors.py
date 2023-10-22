"""
Algorithm Used: Dutch National Flag Algorithm
question link: https://leetcode.com/problems/sort-colors/
"""

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #solved using Dutch national flag algorithm

        low = 0
        mid = 0
        high = len(nums)-1

        while mid <= high:
          if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
          elif nums[mid] == 1:
            mid += 1
          else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1

    