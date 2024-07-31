"""
question link: https://leetcode.com/problems/frequency-of-the-most-frequent-element/

approach:
1. sort the array
2. find the prefix sum of the array
3. for each element in the array, find the maximum subarray sum with k elements using (nums[r]*window_lenght <= total_sum+ k)
4. return the maximum subarray sum
"""

from typing import List

#sliding window approach
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        res = 0
        curr_sum = 0
        nums.sort()
        while r < len(nums):
            curr_sum += nums[r]
            if nums[r]*(r-l+1) <= curr_sum + k:
                res = max(res, r-l+1)
            else:
                curr_sum -= nums[l]
                l += 1
            r += 1
        return res
    
res = Solution().maxFrequency([3,5,6,9,11,20,14,60], 9)
print(res)