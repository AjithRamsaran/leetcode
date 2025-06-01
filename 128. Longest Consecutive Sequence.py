from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets = set(nums)
        res = 0
        for i in sets:
            if i - 1 not in sets:
                e = i + 1
                while e in sets:
                    e += 1
                if res < e - i:
                    res = e - i
        return res


