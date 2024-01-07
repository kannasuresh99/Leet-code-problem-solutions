#my solution
class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        length = 0
        breadth = len(height) - 1
        while length != breadth:
            base = breadth - length
            tall = min(height[breadth],height[length])
            area = base*tall
            if area > max_area:
                max_area = area
            if height[length] > height[breadth]:
                breadth -= 1
            elif height[breadth] > height[length]:
                length += 1
            elif height[breadth] == height[length]:
                length += 1
        return max_area
        
res = Solution()
result = res.maxArea([1,4,3,5,6,7,8,9,11,10,11,22])
print(result)