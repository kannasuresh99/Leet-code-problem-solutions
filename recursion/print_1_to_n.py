def OneToN(i, N):
    if i > N:
        return
    print(i)
    return OneToN(i+1, N)

print("1 to N")
print("-----------")
OneToN(1, 50)
print()

def NToOne(N, i):
    if N < i:
        return
    print(N)
    return NToOne(N-1, i)

print("N to 1")
print("-----------")
NToOne(50,1)

class Solution:
    def printNos(self,N):
        if N == 1:
            print(1)
            return
        self.printNos(N-1)
        print(N)