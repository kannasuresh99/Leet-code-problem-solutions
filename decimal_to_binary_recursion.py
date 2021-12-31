def decimal_to_binary(num):
    if num == 1:
        return '1'
    else:
        remainder = str(num%2)
        quotient = num // 2
        return decimal_to_binary(quotient)+remainder

print(decimal_to_binary(1356))