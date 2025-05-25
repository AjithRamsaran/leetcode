#time taken to solve and understand: 45 mins
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        l = r = 0
        while r < n - 1:
            farthest = l 
            for i in range(l, r + 1):
                if farthest < i + nums[i]:
                    farthest = i + nums[i]
            l = r + 1
            r = farthest
            res += 1
        return res
