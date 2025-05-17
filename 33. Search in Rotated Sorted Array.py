#time taken solve:  mins
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # l = 0
        # r = n -1
        # while l < r:
        #     m = (r + l)//2
        #     if nums[m] == target:
        #         return m
        #     if nums[m] < nums[r] and target < nums[m]:
        #         r = m
        #     elif nums[m] < nums[r] and target > nums[m]:
        #         l = m + 1
        #     elif nums[m] > nums[r] and target < nums[m]:
        #         r = m
        #     else:
        #         l = m + 1
        # return -1
    
s = Solution()
print(s.search([2,1],3))
print(s.search([3,1,2], 1))
print(s.search([4,5,6,7,0,1,2], 4))
print(s.search([11,13,15,17, -11, -12, 15], -12))
print(s.search([-17,-15,-13,-11, 11, 12, 15], 11))

print(type([]))