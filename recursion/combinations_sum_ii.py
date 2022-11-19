class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()

        def combSum(index, candidates, subseq_arr, target):
            if target == 0:
                result.append(subseq_arr[:])
                return
            
            for i in range(index, len(candidates)):
                if i > index and (candidates[i] == candidates[i-1]):
                    continue
                if candidates[i] > target:
                    break
                subseq_arr.append(candidates[i])
                combSum(i+1, candidates, subseq_arr, target-candidates[i])
                subseq_arr.pop()
            return
        combSum(0, candidates, [], target)
        return result
            
                
res = Solution().combinationSum2([1,1,1,2,2,3,4,5,6], 8)
print(res)