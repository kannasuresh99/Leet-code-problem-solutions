
def longestSubarrayWithSumK(a , k) -> int:
    # Write your code here
    i = 0
    max_len = 0
    curr_sum = a[0]

    for j in range(1, len(a)):
        curr_sum += a[j]

        while i < len(a) and curr_sum > k:
            curr_sum -= a[i]
            i += 1
        
        if curr_sum == k:
            max_len = max(max_len, j-i+1)
        
    return max_len


res = longestSubarrayWithSumK([1, 2, 3, 4, 5], 9)
print(res)