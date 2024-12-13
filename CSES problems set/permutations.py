def find_permutation(n):
    if n == 2 or n == 3:
        print("NO SOLUTION")
    else:
        # Print even numbers first
        for num in range(2, n + 1, 2):
            print(num, end=" ")
        
        # Print odd numbers
        for num in range(1, n + 1, 2):
            print(num, end=" ")

n = int(input())
find_permutation(n)
