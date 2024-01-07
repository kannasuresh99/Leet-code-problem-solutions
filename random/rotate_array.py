from typing import List

class Solution:
    def reverse_arr(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        
        #to handle k values greater than len of nums
        k = k%len(nums)
        
        #reverse the entire array
        nums.reverse()

        #reverse the first k elements of the reversed array
        left = 0
        right = k-1

        self.reverse_arr(nums, left, right)

        #reverse last k elements of the reversed array
        left = k
        right = len(nums)-1

        self.reverse_arr(nums, left, right)

        return
