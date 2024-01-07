def sum_of_natural_numbers(n):
    if n >=0 and type(n) == int:
        if n in {0,1}:
            return n
        else:
            return n+sum_of_natural_numbers(n-1)
    else:
        return "Enter a positive integer"


res = sum_of_natural_numbers(100)
print(res)