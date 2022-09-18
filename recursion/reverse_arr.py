def swap(arr, left, right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    return arr


def revArr(arr, start, end):
    if start <= end:
        return arr
    swap(arr, start, end)
    ans = revArr(arr, start+1, end-1)
    return ans


print(revArr([5,4,3,2,1,0],0,5))