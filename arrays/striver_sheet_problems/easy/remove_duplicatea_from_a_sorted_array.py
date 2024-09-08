from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> bool:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] == nums[i]:
                continue
            nums[i+1] = nums[j]
            i += 1

nums = [1,1,1,2,2,3,3,3,3,3,4,4,4,4]
res = Solution().removeDuplicates(nums)
print(nums[:res])