#12321
def isPalindrome(str):
    print("in ",str)
    if len(str) <= 1:
        return True
    if str[0] != str[-1]:
        return False
    
    ans = isPalindrome(str[1:len(str)-1])
    print("out ", str[1:len(str)-1], ans)
    return ans

print(isPalindrome("7896543456987"))