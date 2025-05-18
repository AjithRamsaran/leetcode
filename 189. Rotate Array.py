#time taken solve: 30-45 mins
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        def reverse(l, r):
            while (l < r):
                nums[l], nums[r]  = nums[r],nums[l]
                l += 1
                r -= 1
        reverse(0, n -1)
        reverse(0, k -1)
        reverse(k, n -1)
        print(nums)
s = Solution()
s.rotate([1,2,3,4,5,6,7], 3)