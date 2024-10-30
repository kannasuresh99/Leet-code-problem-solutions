#User function Template for python3

class Solution:
    def recurse(self, A, idx):
        # base cases
        if idx == len(A)-1:
            return True

        if A[idx] == 0:
            if idx != len(A)-1:
                return False
            return True
            
        for idx_jump in range(1, A[idx]+1):
            if self.recurse(A, idx+idx_jump):
                return True
        return False
        
    def canReach(self, A, N):
        # code here 
        return 1 if self.recurse(A, 0) else 0
        
