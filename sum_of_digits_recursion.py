def sum_of_digits(integer):
    if integer >=0 and type(integer) == int:
        if integer in {0,1,2,3,4,5,6,7,8,9}:
            return integer
        else:
            sum = integer%10
            return sum+sum_of_digits(integer//10)
    else:
        return "Enter a positive integer"

print(sum_of_digits(854))