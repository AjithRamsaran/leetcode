#time taken solve: 45 mins
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            m = (r + l) //2
            if nums[m] >= nums[0]:
                l = m + 1
            else:
                r = m
        return min(nums[0], nums[l])
        
s = Solution()
print(s.findMin([2,1]))
print(s.findMin([3,1,2]))
print(s.findMin([4,5,6,7,0,1,2]))
print(s.findMin([11,13,15,17, -11, -12, 15]))