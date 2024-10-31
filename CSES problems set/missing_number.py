def find_missing_number(nums, n):
    expected_total = (n*(n+1))//2
    actual_total = sum(nums)
    return expected_total - actual_total

total_numbers = int(input())
nums = list(map(int, input().split()))
print(find_missing_number(nums, total_numbers))
