from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1 for _ in range(n)]

        left_product = 1
        for i in range(n):
            res[i] *= left_product
            left_product *= nums[i]

        right_product = 1
        for j in range(n-1, -1, -1):
            res[j] *= right_product
            right_product *= nums[j]

        return res 
    

