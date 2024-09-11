class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        #Your code here
        left = 0
        right = N-1
        
        while left <= right:
            mid = (left+right)//2

            if arr[mid] == K:
                return 1
            
            if arr[mid] < K:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

res = Solution().searchInSorted([1,2,3,4,5], 5, 4)
print(res)