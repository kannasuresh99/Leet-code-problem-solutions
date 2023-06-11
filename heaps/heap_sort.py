
def heapify(arr, n, i):
    largest = i #initially setting i as the largest index
    left = 2*i+1
    right = 2*i+2

    if left < n and arr[left] > arr[i]:
        largest = left
    
    if right < n and arr[right] > arr[i]:
        largest = right

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)
	#starting with the last parent node then to the first
    for i in range(n //2 -1, -1, -1):
        heapify(arr, n, i)

    for j in range(n-1, 0, -1):
        (arr[j],arr[0]) = (arr[0],arr[j])
        heapify(arr, j, 0)

arr = [12, 11, 13, 5, 6, 7, 8]
heapSort(arr)
n = len(arr)
print('Sorted array is')
for i in range(n):
	print(arr[i], end=" ")