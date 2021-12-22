#my solution
class Solution:

    def get_first_value_index(self,nums,target):
        result = []
        first_index_value = None
        if target < 0:
            for index in range(0,len(nums)):
                if nums[index] != None and nums[index] > target:
                    first_index_value = index
                    result.append(first_index_value)
                    break
        else:
            if target == 0:
                for index in range(0,len(nums)):
                    if nums[index] <= 0:
                        result.append(index)
                        break
            else:
                max_value = max(filter(lambda v: v is not None, nums))
                min_value = min(filter(lambda v: v is not None, nums))
                if min_value > 0:
                    while first_index_value == None:
                        if max_value < target:
                            first_index_value = nums.index(max_value)
                            result.append(first_index_value)
                            break
                        else:
                            nums[nums.index(max_value)] = None
                            max_value = max(filter(lambda v: v is not None, nums))
                elif min_value < 0:
                    first_index_value = nums.index(min_value)
                    result.append(first_index_value)                        
        return result

    def twoSum(self, nums, target):
        result = []
        second_value = None
        second_index_value = None
        while second_index_value == None:
            result = self.get_first_value_index(nums,target)
            second_value = target - nums[result[0]]
            for i,val in enumerate(nums):
                if i != result[0] and val == second_value:
                    second_index_value = i
                    result.append(second_index_value)
            print(nums,target,result,second_value,second_index_value)
            nums[result[0]] = None
        result.sort()
        return result

res = Solution()
result = res.twoSum([2,1,9,4,4,56,90,3],8)
print(result)

#solution by leetcode
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
            print(i,complement,hashmap)


res = Solution()
result = res.twoSum([2,1,9,4,4,56,90,3],8)
print(result)