
def printSubsequences(arr, subseq_arr, idx, n):
    #print("debug: ", "incoming index: ", idx, subseq_arr, end=" ")
    if idx == n:
        #print()
        if subseq_arr == []:
            print("{}")
        for num in subseq_arr:
            print(num, end=" ")
        print()
        return
    subseq_arr.append(arr[idx])
    #print("index being passed for 1st call: ", idx+1, subseq_arr)
    printSubsequences(arr, subseq_arr, idx+1, n)
    #print("poping out last element when the idx is: ", idx, subseq_arr)
    subseq_arr.pop()
    #print("index being passed for 2nd call: ", idx+1, subseq_arr)
    printSubsequences(arr, subseq_arr, idx+1, n)

arr = [3, 1, 2, 2]
printSubsequences(arr, [], 0, 4)