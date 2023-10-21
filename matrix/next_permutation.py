"""question link: https://leetcode.com/problems/next-permutation/"""

from typing import List

class Solution:
    def reverse_subarray_in_place(self, start, end, arr):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        return

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #finding the breakpoint
        n = len(nums)
        idx = -1

        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                idx = i
                break
        
        #edge case for last permutation
        if idx == -1:
            nums.reverse()
            return
        
        #finding the first greater element to swap
        for i in range(n-1, idx, -1):
            if nums[i] > nums[idx]:
                nums[idx], nums[i] = nums[i], nums[idx]
                break
        
        #reversing the elements after the breakpoint
        self.reverse_subarray_in_place(idx+1, n-1, nums)

