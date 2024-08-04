"""
Insertion Sort
Given an unsorted array of integers, sort the array into a non-decreasing order using the Insertion Sort algorithm.
Algorithm:
1. Start from the second element of the array and compare the current element with the previous element of the array.
2. If the current element is less than the previous element of the array, swap them.
3. Repeat step 2 for all the elements of the array.
Example 1:
Input:
N = 10
arr[] = {9, 7, 8, 3, 2, 1, 5, 4, 6, 0}
Output:
0 1 2 3 4 5 6 7 8 9
Explanation:
After step 1, the array will be {7, 9, 8, 3, 2, 1, 5, 4, 6, 0}.
After step 2, the array will be {7, 8, 9, 3, 2, 1, 5, 4, 6, 0}.
After step 3, the array will be {3, 7, 8, 9, 2, 1, 5, 4, 6, 0}.
After step 4, the array will be {2, 3, 7, 8, 9, 1, 5, 4, 6, 0}.
After step 5, the array will be {1, 2, 3, 7, 8, 9, 5, 4, 6, 0}.
After step 6, the array will be {1, 2, 3, 5, 7, 8, 9, 4, 6, 0}.
After step 7, the array will be {1, 2, 3, 4, 5, 7, 8, 9, 6, 0}.
After step 8, the array will be {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}.
After step 9, the array will be {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}.
The sorted array is {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}.
"""

class Solution:
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        #code here
        for i in range(0, n):
            j = i
            while j > 0 and alist[j] < alist[j-1]:
                temp = alist[j]
                alist[j] = alist[j-1]
                alist[j-1] = temp
                j -= 1

