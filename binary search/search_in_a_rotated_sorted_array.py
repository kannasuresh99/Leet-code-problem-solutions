from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target < nums[0] and target > nums[-1]:
            return -1

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right)//2

            if target == nums[mid]:
                return mid
            #check if mid belongs to left half
            elif nums[left] <= nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            #check if mid belongs to right half
            else:
                if target  <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
    
