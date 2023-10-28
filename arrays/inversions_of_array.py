from os import *
from sys import *
from collections import *
from math import *

class CountInversions:
    def merge_sort(self, arr, low, high):
        cnt = 0
        if low == high:
            return cnt
        
        mid = (low + high)//2
        cnt += self.merge_sort(arr, low, mid)
        cnt += self.merge_sort(arr, mid+1, high)
        cnt += self.__merge_arr(arr, low, mid, high)
        return cnt
    
    
    def __merge_arr(self, arr, low, mid, high):
        left = low
        right = mid + 1
        temp = []
        
        cnt = 0
        
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                cnt += (mid-left)+1
                right += 1
        
        while left <= mid:
            temp.append(arr[left])
            left += 1
        
        while right <= high:
            temp.append(arr[right])
            right += 1
        
        for i in range(low, high+1):
            arr[i] = temp[i - low]
        
        return cnt


def getInversions(arr, n) :
	# Write your code here.
	return CountInversions().merge_sort(arr, 0, n-1)

# Taking input using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))

