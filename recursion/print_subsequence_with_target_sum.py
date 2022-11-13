
def printSubsequencesWithGivenSum(arr, subseq_arr, idx, target_sum, seq_sum):
    if idx == len(arr):
        if seq_sum == target_sum:
            for num in subseq_arr:
                print(num, end=" ")
            print()
        return
    subseq_arr.append(arr[idx])
    seq_sum += arr[idx]
    printSubsequencesWithGivenSum(arr, subseq_arr, idx+1, target_sum, seq_sum)
    subseq_arr.pop()
    seq_sum -= arr[idx]
    printSubsequencesWithGivenSum(arr, subseq_arr, idx+1, target_sum, seq_sum)


arr = [1,2,3,4,5,6,99,22,90,11]
sum = 24
printSubsequencesWithGivenSum(arr, [], 0, sum, 0)