from typing import List


class Solution:
    def __reverse_sub_list(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n

        self.__reverse_sub_list(nums, 0, n-k-1)
        self.__reverse_sub_list(nums, n-k, n-1)
        self.__reverse_sub_list(nums, 0, n-1)

nums = [1,2,3,4,5,6,7]
Solution().rotate(nums, 3)
print(nums)