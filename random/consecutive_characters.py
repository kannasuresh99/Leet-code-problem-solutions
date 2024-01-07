#my solution
class Solution:
    def getSubStrings(self,word):
        count = 1
        unique_str = ['']
        count_list = []
        for index in range(0,len(word)-1):
            if word[index] == word[index+1]:
                if word[index] != unique_str[-1]:
                    count_list.append(count)
                    unique_str.append(word[index])
                    count = 1
                count += 1
            unique_str.append(word[index])
        count_list.append(count)
        return max(count_list)

res = Solution()
result = res.getSubStrings("bacacccbba")
print(result)

#solution given by leetcode
class Solution:
    def maxPower(self, s: str) -> int:
        count = 0
        max_count = 0
        previous = None
        for c in s:
            if c == previous:
                # if same as previous one, increase the count
                count += 1
                print(c,previous,count,max_count)
            else:
                # else, reset the count
                previous = c
                count = 1
                print(c,previous,count,max_count)
            max_count = max(max_count, count)
        return max_count

res = Solution()
result = res.maxPower("bacacccbba")
print(result)