#time taken to solve: 15 mins
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # n = len(nums) / 2
        # c = defaultdict(int)
        # for i in nums:
        #     c[i] += 1  
        #     if c[i] >= n:
        #         return i
        majority = 0
        res = 0
        for i in nums:
            if majority == 0:
                res = i
            majority += 1 if res == i else -1
        return res