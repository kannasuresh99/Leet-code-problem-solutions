
def CountSubsequencesWithGivenSum(arr, idx, target_sum, seq_sum):
    if idx == len(arr):
        if seq_sum == target_sum:
            return 1
        return 0

    seq_sum += arr[idx]
    l = CountSubsequencesWithGivenSum(arr, idx+1, target_sum, seq_sum)
    seq_sum -= arr[idx]

    r = CountSubsequencesWithGivenSum(arr, idx+1, target_sum, seq_sum)
    return l+r


arr = [1,2,1]
sum = 2
print(CountSubsequencesWithGivenSum(arr, 0, sum, 0))