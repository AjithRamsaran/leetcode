#time taken solve: 45 mins
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        maxi = nums[0]
        for i,val in enumerate(nums[1:],1):
            temp = min(val, curMin * val, curMax * val)
            curMax = max(val, curMin * val, curMax * val)
            curMin = temp
            maxi = max(maxi, curMax)
        return maxi
s = Solution()
print(s.maxProduct([2,3,-2,4]))
print(s.maxProduct([-2,0,-1]))
print(s.maxProduct([5,4,-1,7,8,-2]))
print(s.maxProduct([5,4,-1,7,8]))
print(s.maxProduct([2,-5,-2,-4, 3]))
