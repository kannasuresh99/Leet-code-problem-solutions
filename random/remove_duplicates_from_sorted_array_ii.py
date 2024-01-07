from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 2
        r = 2
        while r < len(nums):
            if nums[l - 2] != nums[r]:
                nums[l] = nums[r]
                l += 1
            r += 1
        return l

