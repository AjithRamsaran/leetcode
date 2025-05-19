#time taken solve: 25 mins
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        prev = nums[0] if nums[0] > 0 else 0
        for i in nums[1:]:
            prev = prev + i
            maxi = max(maxi, prev)
            if prev < 0:
                prev = 0
        return maxi
s = Solution()
print(s.maxSubArray(([-2,1,-3,4,-1,2,1,-5,4])))
print(s.maxSubArray([1]))
print(s.maxSubArray(([5,4,-1,7,8])))
print(s.maxSubArray(([-1,-2])))