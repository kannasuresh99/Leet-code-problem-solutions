"""
Solved using Moore's Voting Algorithm

Explanation of  Moore's Voting Algorithm:
    - We can solve this problem using Moore's Voting Algorithm
    - We can iterate through the array and maintain two variables candidate and count
    - If the count is equal to 0, we can update the candidate to the current element
    - If the candidate is equal to the current element, we can increment the count
    - If the candidate is not equal to the current element, we can decrement the count
    - Finally, we can return the candidate
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #using Moore's Voting algorithm
        majority_element = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == majority_element:
                count += 1
            else:
                count -= 1

            if count == 0:
                majority_element = nums[i]
                count = 1
        
        return majority_element

res = Solution().majorityElement([2,2,1,1,1,2,2])
print(res)
