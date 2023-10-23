

"""
Algorithm Used:
        s - sn = (1+1+2+3+4+5) - (1+2+3+4+5+6)
        s2 - s2n = (1**2 + 1**2 + 2**2 + ).............
        x - y = 1 - 5
        x + y = -24//(x - y)
        x + y = 6
        x = (x+y) + (x-y)//2
        x = 1 repeating number
        y = x-y-x
        y = 5 missing number
        
question link: https://www.codingninjas.com/studio/problems/873366
"""

def missingAndRepeating(arr, n):
    # Write your code here
    sn = (n*(n+1))//2
    s2n = (n*(n+1)*(2*n + 1))//6
    s = 0
    s2 = 0

    for num in arr:
        s += num
        s2 += num*num
    
    x_minus_y = s - sn
    x_plus_y = (s2-s2n)//x_minus_y
    x = (x_minus_y + x_plus_y)//2
    y = x - x_minus_y
    return [y, x]
    
