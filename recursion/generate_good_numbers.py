"""
question link: https://leetcode.com/problems/count-good-numbers/
"""

class Solution:
    def recurse(self, idx, n, rec_arr, res):
        even_numbers = [0, 2, 4, 6, 8]
        prime_numbers = [2, 3, 5, 7]

        if len(rec_arr) >= n:
            res.append("".join(map(str, rec_arr[:])))
            return
        
        if idx % 2 == 0:
            for num in even_numbers:
                rec_arr.append(num)
                self.recurse(idx+1, n, rec_arr, res)
                rec_arr.pop()
        elif idx % 2 == 1:
            for prime_num in prime_numbers:
                rec_arr.append(prime_num)
                self.recurse(idx+1, n, rec_arr, res)
                rec_arr.pop()
        return

    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5
        
        res = []
        for i in [0,2,4,6,8]:
            rec_arr = [i]
            self.recurse(i+1, n, rec_arr, res)
        
        for combo in res:
            print(combo)
        #multiply by 5 because, there are 5 single digit even numbers from 0 to 10
        return len(res)

res = Solution().countGoodNumbers(3)
print(res)