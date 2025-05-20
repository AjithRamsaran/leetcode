from typing import List
import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        n = len(nums)

        r = n - 1

        while (l <= r):
            m = (r + l) // 2
            print(m)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1