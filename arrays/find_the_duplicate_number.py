"""
Algorithm Used: Linkedlist cycle detection
question link: https://leetcode.com/problems/find-the-duplicate-number/
"""

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #using linkedlist cycle detection technique to solve this
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        fast = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

