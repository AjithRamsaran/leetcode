#time taken solve: 5 mins
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        for i,val in enumerate(nums):
            if target - val in pair:
                return [pair[target - val], i]
            pair[val] = i
s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3,2,4], 6))
print(s.twoSum([3,3],6))