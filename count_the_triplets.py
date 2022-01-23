class Solution:
    def countTriplet(self, arr, n):
        temp = arr
        temp_index = 0
        triplets_count = 0
        ignore_second_value = []
        while temp_index < n:
            first_value = temp[temp_index]
            for i in range(0,n):
                if i!= temp_index:
                    second_value = arr[i]
                    if second_value not in set(ignore_second_value):
                        third_value = first_value + second_value
                    else:
                        third_value = None
                    if third_value in arr:
                        triplets_count += 1
                        ignore_second_value.append(first_value)
            temp_index += 1
        return triplets_count

res = Solution()
result = res.countTriplet([1,5,3,2],4)
print(result)