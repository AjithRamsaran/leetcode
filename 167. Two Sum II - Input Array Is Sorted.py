#time taken solve: 5-7 mins
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n - 1
        while (l < r):
            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1, r+1]
            if total > target:
                r -= 1
            else:
                l += 1
        return []
s = Solution()
print(s.twoSum([2,7,11,15],9))
print(s.twoSum([2,3,4], 6))
print(s.twoSum([-1,0], -1))