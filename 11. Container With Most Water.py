from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxi = 0
        while l < r:
            b = r - l
            a = 0
            if height[l] < height[r]:
                a = height[l]
                l += 1
            else :
                a = height[r]
                r -= 1    
            if maxi < a * b:
                maxi = a * b
        return maxi
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7])) 
print(s.maxArea([1,1]))
print(s.maxArea([4, 3, 2, 1, 4])) 
print(s.maxArea([1,3,2,5,25,24,5]))           