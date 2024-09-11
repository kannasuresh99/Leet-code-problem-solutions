#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        i, j = 0, 0
        
        union_result = []
        
        while i < n and j < m:
            while i > 0 and i < n and arr1[i] == arr1[i-1]:
                i += 1
            
            while j > 0 and j < m and arr2[j] == arr2[j-1]:
                j += 1
            
            if i >= n or j >= m:
                break
            
            if arr1[i] < arr2[j]:
                union_result.append(arr1[i])
                i += 1
            elif arr1[i] > arr2[j]:
                union_result.append(arr2[j])
                j += 1
            else:
                union_result.append(arr1[i])
                i += 1
                j += 1
        
        while i < n:
            if i == 0 or arr1[i] != arr1[i-1]:
                union_result.append(arr1[i])
            i += 1
        
        while j < m:
            if j == 0 or arr2[j] != arr2[j-1]:
                union_result.append(arr2[j]) 
            j += 1
        
        return union_result


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        ob=Solution()
        li = ob.findUnion(a,b,n,m)
        for val in li:
            print(val, end = ' ')
        print()