from typing import List

class Solution:
    def rob_house_linear(self, nums):
        n = len(nums)
        prev2 = nums[0]
        prev = nums[0]

        for i in range(1, n):
            pick = nums[i]
            if i > 1:
                pick += prev2
            not_pick = prev
            curr = max(pick, not_pick)
            prev2 = prev
            prev = curr

        return prev

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        #excluding last house
        ans1 = self.rob_house_linear(nums[:len(nums)-1])

        #excluding first house
        ans2 = self.rob_house_linear(nums[1:])

        return max(ans1, ans2)


