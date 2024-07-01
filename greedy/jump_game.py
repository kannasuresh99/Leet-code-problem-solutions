"""
question link: https://leetcode.com/problems/jump-game/
"""

"""
Approach: Greedy
Time complexity: O(n)
Space complexity: O(1)

The idea is to start from the end of the array and keep track of the goal. The goal is to reach the first index of the array.
If we can reach the goal from the current index, then we update the goal to the current index.
If the goal is 0, then we can reach the first index of the array.
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0
        