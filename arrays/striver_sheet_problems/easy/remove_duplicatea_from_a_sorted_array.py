from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] == nums[i]:
                continue
            nums[i+1] = nums[j]
            i += 1

nums = [1,1,1,2,2,3,3,3,3,3,4,4,4,4]
Solution().check(nums)
print(nums)