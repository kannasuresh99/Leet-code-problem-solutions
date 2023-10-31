"""
Algorithm Used: Merge Sort Algorithm
question link: https://leetcode.com/problems/reverse-pairs/
"""

from typing import List

class Solution:
    def merge_sort(self, arr, low, high):
        cnt = 0
        if low == high:
            return cnt
        
        mid = (low+high)//2

        cnt += self.merge_sort(arr, low, mid)
        cnt += self.merge_sort(arr, mid+1, high)
        cnt += self.count_pairs(arr, low, mid, high)
        self.merge_arr(arr, low, mid, high)
        return cnt
    
    def count_pairs(self, arr, low, mid, high):
        cnt = 0
        right = mid + 1

        for i in range(low, mid+1):
            while right <= high and arr[i] > (2*arr[right]):
                right += 1
            cnt = cnt + (right - (mid + 1))
        return cnt

    def merge_arr(self, arr, low, mid, high):
        left = low
        right = mid + 1
        temp = []

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        
        while left <= mid:
            temp.append(arr[left])
            left += 1
        
        while right <= high:
            temp.append(arr[right])
            right += 1
        
        for i in range(low, high+1):
            arr[i] = temp[i-low]


    def reversePairs(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        return self.merge_sort(nums, low, high)

