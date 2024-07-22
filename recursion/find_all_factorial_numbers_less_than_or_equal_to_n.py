"""
question link: https://www.geeksforgeeks.org/problems/find-all-factorial-numbers-less-than-or-equal-to-n3548/0
"""

class Solution:
    def factorialNumbers(self, n):
        res = []
        def recurse(num, fact_num):
            if fact_num > n:
                return res
            res.append(fact_num)
            curr_num = num+1
            fact = curr_num*fact_num
            recurse(curr_num, fact)
        recurse(1, 1)
        return res
    	    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends