def multiply(a,b):
    if b == 0:
        return 0
    if b > 0:
        return a+multiply(a,b-1)
    elif b < 0:
        return -(multiply(a,-b))

print(multiply(5,-4))