#parameterized way
def sumOfN(n, sum):
    if n < 1:
        return sum
    ans = sumOfN(n-1, sum+n)
    return ans

print(sumOfN(5, 0))

#functional way
def sumOfN(n):
    if n < 1:
        return n
    ans = n + sumOfN(n-1)
    return ans

print(sumOfN(5))