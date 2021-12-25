class Solution:
    #I have used Square Root by Repeated Subtraction Method to find the square root
    def mySqrt(self, x: int) -> int:
        square_root = 0
        odd_number_value = 1
        if x == 0:
            return 0
        if x == 1:
            return 1
        while x >= 0:
            x = x - odd_number_value
            odd_number_value += 2
            square_root += 1
        square_root = square_root - 1
        return square_root

res = Solution()
result = res.mySqrt(10000)
print(result)
