from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        left = 0
        right = 1
        k = 1

        while left < len(nums) and right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                temp = nums[left+1]
                nums[left+1] = nums[right]
                nums[right] = temp
                left += 1
                right += 1
                k += 1

        return k

