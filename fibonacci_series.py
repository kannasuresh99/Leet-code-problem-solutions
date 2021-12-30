def fibonacci(n):
    if n >= 0 and type(n) == int:
        if n in {1,0}:
            return n
        else:
            return fibonacci(n-1)+fibonacci(n-2)
    else:
        return "Enter a positive integer"

print(fibonacci(2.8))
    