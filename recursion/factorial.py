#parameterized way
def fact(n, factorial):
    if n < 1:
        return factorial
    ans = fact(n-1, factorial*n)
    return ans

print(fact(5, 1))

#functional way
def fact(n):
    if n <= 1:
        return 1
    ans = n*fact(n-1)
    return ans

print(fact(5))