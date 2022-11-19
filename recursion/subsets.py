class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        def subsetsRecursion(idx, nums, subseq_arr):
            if idx == len(nums):
                result.append(subseq_arr[:])
                return
            
            subseq_arr.append(nums[idx])
            subsetsRecursion(idx+1, nums, subseq_arr)
            subseq_arr.pop()
            
            subsetsRecursion(idx+1, nums, subseq_arr)
        
        subsetsRecursion(0, nums, [])
        return result
        
res = Solution().subsets([3,1,2,4])
print(res)