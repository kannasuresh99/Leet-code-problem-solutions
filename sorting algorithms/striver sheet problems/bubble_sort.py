"""
Bubble Sort
Given an unsorted array of integers, sort the array into a non-decreasing order using the Bubble Sort algorithm.
Algorithm:
1. Start from the first element of the array and compare the current element with the next element of the array.
2. If the current element is greater than the next element of the array, swap them.
3. If the current element is less than the next element, move to the next element.
4. Repeat step 1 and step 2 for all the elements of the array.
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
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        # code here
        for i in range(n-1, 0, -1):
            for j in range(0, i):
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr, n)
        for i in arr:
            print(i,end=' ')
        print()

# } Driver Code Ends