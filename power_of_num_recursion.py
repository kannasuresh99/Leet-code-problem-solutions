def power_of_num(num,power):
    if power < 0:
        power *= -1
        if num == 0:
            return 0
        if power == 1:
            return 1/num
        if power == 0:
            return 1
        else:
            return 1/(num*power_of_num(num,power-1))
    else:
        if num == 0:
            return 0
        if power == 1:
            return num
        if power == 0:
            return 1
        else:
            return num*power_of_num(num,power-1)

print(power_of_num(10,-4))