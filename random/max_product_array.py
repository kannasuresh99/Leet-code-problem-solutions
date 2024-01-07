def maxProductArray(arr):
    max_value = max(arr)
    max_value_index = arr.index(max_value)
    max_product = 0
    for i in range(0,len(arr)):
        if i != max_value_index:
            if arr[i]*max_value > max_product:
                max_product = arr[i]*max_value
    return max_product

def maxProductArrayMethodTwo(arr):
    first_max_value = max(arr)
    first_max_value_index = arr.index(first_max_value)
    arr.pop(first_max_value_index)
    second_max_value = max(arr)
    max_product = first_max_value*second_max_value
    return max_product


res = maxProductArray([1,3,4,9,11,2,4,22,23])
print('1:',res)
res = maxProductArrayMethodTwo([1,3,4,9,11,2,4,23,22])
print('2:',res)