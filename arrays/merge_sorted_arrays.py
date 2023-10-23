"""question link: https://leetcode.com/problems/merge-sorted-array/"""

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1 #nums1 last index except zeros
        j = n - 1 #nums2 last index
        k = m + n - 1 #nums1 last index

        while j >= 0:
            if i >=0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1

        