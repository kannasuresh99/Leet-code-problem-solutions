class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) > len(nums2):
            looping_array = nums2
            non_looping_array = nums1
        else:
            looping_array = nums1
            non_looping_array = nums2
            temp = m
            m = n
            n = temp
        if len(looping_array) == 1:
            if looping_array[0] == 0:
                nums1 = non_looping_array
                return nums1
        for i in range(0,len(looping_array)):
            if looping_array[i] in non_looping_array:
                adjacent_index = non_looping_array.index(looping_array[i])
                non_looping_array.insert(adjacent_index+1,looping_array[i])
                m += 1
            else:
                if looping_array[i] > non_looping_array[m-1]:
                    non_looping_array[m] = looping_array[i]
                    m += 1
                elif looping_array[i] < non_looping_array[0]:
                    non_looping_array.insert(0,looping_array[i])
                else:
                    for j in range(0,len(non_looping_array)-1):
                        if looping_array[i] > non_looping_array[j] and looping_array[i] < non_looping_array[j+1]:
                            non_looping_array.insert(j+1,looping_array[i])
                            m += 1
        nums1 = non_looping_array[:m]
        print(nums1)
        return nums1


res = Solution()
result = res.merge([0]
,0
,[1]
,1)
print(result)