#my solution
class Solution:
    def get_max_count(self,nums):
        count = 0
        max_sum = nums[0]
        for i in range(0,len(nums)-1):
            if nums[i+1] >= nums[i]:
                if nums[i+1] >= max_sum:
                    max_sum = nums[i+1]
                else:
                    count += 1
                continue
            else:
                count += 1
        return count
    
    def get_min_count(self,nums):
        count = 0
        min_sum = nums[len(nums)-1]
        for i in range(len(nums)-1,0,-1):
            if nums[i-1] <= nums[i]:
                if nums[i-1] <= min_sum:
                    min_sum = nums[i-1]
                else:
                    count += 1
                continue
            else:
                count += 1
        return count

    def checkPossibility(self, nums: list[int]) -> bool:
        max_count = self.get_max_count(nums)
        min_count = self.get_min_count(nums)
        print(min_count,max_count)
        if max_count <= 1 or min_count <= 1:
            return True
        else:
            return False
        
        

res = Solution()
result = res.checkPossibility([1,1,1])
print(result)