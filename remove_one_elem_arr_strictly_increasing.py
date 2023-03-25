class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        i = 0
        nums.append(float('inf'))
        n = len(nums) - 1
        left = 0
        flag = False

        while i < n:
            mid = nums[i]
            right = nums[i+1]
            if left < mid < right:
                left = mid
            else:
                if flag:
                    return False
                flag = True
                if right <= left:
                    left = mid
                    i += 1
            i += 1
        
        return True