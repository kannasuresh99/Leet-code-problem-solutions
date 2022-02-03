class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        unique_values = set()
        difference = float('inf')
        for i in range(0,len(nums)):
            if nums[i] in unique_values:
                start_index = nums.index(nums[i])+1
                while nums[i] in nums[start_index:]:
                    val_place = nums.index(nums[i],start_index)
                    difference = min(abs(start_index-1-val_place),difference)
                    start_index = val_place + 1
                    
                if difference <= k:
                    return True
            unique_values.add(nums[i])
        return False


res = Solution()
result = res.containsNearbyDuplicate([1,0,1,1,2],1)
print(result)