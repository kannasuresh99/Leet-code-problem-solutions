#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def recurse(self, idx, n, rec_arr, res):
        if idx == n:
            res.append("".join(rec_arr))
            return
        
        rec_arr.append("0")
        self.recurse(idx+1, n, rec_arr, res)
        rec_arr.pop()
        
        if rec_arr and rec_arr[-1] == "1":
            return
        else:
            rec_arr.append("1")
            self.recurse(idx+1, n, rec_arr, res)
            rec_arr.pop()
        
        return
    
    def generateBinaryStrings(self, n):
        # Code here
        res = []
        self.recurse(0, n, [], res)
        return res
        
        
res = Solution().generateBinaryStrings(3)
print(res)

