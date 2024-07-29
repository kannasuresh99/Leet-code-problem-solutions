"""
question link: https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/1
"""

class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, n, p):
        i = 0
        j = 0
        while i < n:
            if arr[i] > 0 and arr[i] <= n:
                j = arr[i] - 1
                if arr[j] < 0:
                    arr[i] = 0
                    arr[j] -= 1
                    i += 1
                else:
                    arr[i] = arr[j]
                    arr[j] = -1
            elif arr[i] > n:
                arr[i] = 0
                i += 1
            else:
                i += 1
        
        for i in range(n):
            arr[i] *= -1

res = Solution().frequencyCount([2, 3, 2, 3, 5], 5, 5)
print(res)