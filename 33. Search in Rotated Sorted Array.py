#time taken solve: 3-4 hours
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n -1
        while l <= r:
            m = (r + l)//2
            if nums[m] == target:
                return m

            #left sorted portion
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1 #nums[l] if nums[l] == target else -1
    
s = Solution()
print(s.search([2,1],3))
print(s.search([3,1,2], 1))
print(s.search([4,5,6,7,0,1,2], 4))
print(s.search([11,13,15,17, -15, -12, -11], -12))
print(s.search([-17,-15,-13,-11, 11, 12, 15], 11))
print(s.search([5,1,3], 5))
print(s.search([5,1,3],3))
print(type([]))