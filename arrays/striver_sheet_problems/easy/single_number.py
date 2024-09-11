from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Given a non-empty array of integers, every element appears twice except for one. Find that single one.

        solution: XOR all the elements in the array. The result will be the single number.
        what is a XOR? XOR is a bitwise operator that returns 1 if the bits are different and 0 if the bits are the same.
        1 XOR 1 = 0
        1 XOR 0 = 1
        0 XOR 1 = 1
        0 XOR 0 = 0
        22 XOR 23 = 1
        22 XOR 22 = 0
        """
        res = 0
        for num in nums:
            res = res^num
        return res
