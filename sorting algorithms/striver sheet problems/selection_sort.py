"""
Selection Sort
Given an unsorted array of integers, sort the array into a non-decreasing order using the Selection Sort algorithm.
Algorithm:
1. Start from the first element of the array and find the smallest element in the array.
2. Swap the smallest element with the first element of the array.
3. Repeat the above steps for the remaining elements of the array.
Example 1:
Input:
N = 5
arr[] = {4, 1, 3, 9, 7}
Output:
1 3 4 7 9
Explanation:
After step 1, the array will be {1, 4, 3, 9, 7}.
After step 2, the array will be {1, 3, 4, 9, 7}.
After step 3, the array will be {1, 3, 4, 7, 9}.
The sorted array is {1, 3, 4, 7, 9}.
"""

class Solution: 
    def select(self, arr, i):
        # code here 
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        return min_index
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(0, n-1):
            min_num_index = self.select(arr, i)
            temp = arr[i]
            arr[i] = arr[min_num_index]
            arr[min_num_index] = temp


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends