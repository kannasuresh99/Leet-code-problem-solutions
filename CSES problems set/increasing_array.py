def find_min_moves(nums, total_numbers):
    min_moves = 0

    for i in range(1, total_numbers):
        if nums[i] < nums[i-1]:
            diff = nums[i-1] - nums[i]
            nums[i] += diff
            min_moves += diff
    
    return min_moves


total_numbers = int(input())
nums = list(map(int, input().split()))
print(find_min_moves(nums, total_numbers))
