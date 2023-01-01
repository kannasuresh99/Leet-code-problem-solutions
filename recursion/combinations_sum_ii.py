class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()
        def CombSum2(idx, arr, subseq_arr, target):
            if target == 0:
                result.append(subseq_arr[:])
                return
            
            for i in range(idx, len(arr)):
                if arr[i] > target:
                    break
                #don't pick up condition
                if (i > idx) and (arr[i] == arr[i-1]):
                    continue
                subseq_arr.append(arr[i])
                CombSum2(i+1, arr, subseq_arr, target-arr[i])
                subseq_arr.pop()
            return
        CombSum2(0, candidates, [], target)
        return result
            
                
res = Solution().combinationSum2([1,1,1,2,2,3,4,5,6], 8)
print(res)
