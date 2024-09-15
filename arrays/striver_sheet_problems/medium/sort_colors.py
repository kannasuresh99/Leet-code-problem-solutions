from typing import List
"""
Solved using Dutch National Flag Algorithm

Thought process behind the solution:
    - Think of an hypothetical array which has only 3 types of elements 0, 1, and 2
    - from index 0 to low-1, we have only 0's
    - from index low to mid-1, we have only 1's
    - from index mid to high, we have elements that are not sorted
    - from index high+1 to n-1, we have only 2's

Algorithm intuition:
    - We can solve this problem using Dutch National Flag Algorithm
    - We can use three pointers low, mid, and high
    - We can iterate through the array using the mid pointer
    - If the mid pointer is pointing to 0, we can swap the mid pointer with the low pointer and increment both low and mid pointer
    - If the mid pointer is pointing to 1, we can increment the mid pointer
    - If the mid pointer is pointing to 2, we can swap the mid pointer with the high pointer and decrement the high pointer
    - We can continue this process until the mid pointer is less than or equal to the high pointer
    - Finally, we can return the sorted array
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums)-1

        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
