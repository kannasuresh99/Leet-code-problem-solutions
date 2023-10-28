
class MergeSort:
    def merge_sort(self, arr, low, high):
        if low == high:
            return
        
        mid = (low + high)//2
        self.merge_sort(arr, low, mid)
        self.merge_sort(arr, mid+1, high)
        self.__merge_arr(arr, low, mid, high)
        return
    
    
    def __merge_arr(self, arr, low, mid, high):
        left = low
        right = mid + 1
        temp = []
        
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        
        while left <= mid:
            temp.append(arr[left])
            left += 1
        
        while right <= high:
            temp.append(arr[right])
            right += 1
        
        for i in range(low, high+1):
            arr[i] = temp[i - low]

arr = [3,1,2,4,1,5,2,6,4]
low = 0
high = len(arr) - 1
MergeSort().merge_sort(arr, low, high)
print(arr)