#my solution
class Solution:
    def searchInsert(self, nums, target):
        middle = len(nums)//2
        left = 0
        right = len(nums)-1
        if target not in nums:
            if nums[0] > target:
                return left
            if nums[-1] < target:
                return right+1
            while left != right:
                if target > nums[middle] and target < nums[middle+1]:
                    return middle+1
                else:
                    if nums[middle] > target:
                        right = middle - 1
                        middle = (left + right)//2
                        middle = 1 if middle == 0 else middle
                    elif nums[middle] < target:
                        left = middle + 1
                        middle = (left + right)//2


        else:
            if nums[0] == target:
                return left
            if nums[-1] == target:
                return right
            while middle != 0:
                if nums[middle] == target:
                    return middle
                elif nums[middle] > target:
                    right = middle - 1
                    middle = (left + right)//2
                    middle = 1 if middle == 0 else middle
                elif nums[middle] < target:
                    left = middle + 1
                    middle = (left + right)//2
        return middle
        

res = Solution()
result = res.searchInsert([1,2,4,6,7],3)
print(result)