#time taken to solve: 30 mins
from typing import List
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [1] * n
        # for i in range(n):
        #     for j in range(i):
        #         if nums[i] > nums[j] and dp[i] < dp[j] + 1:
        #             dp[i] = dp[j] + 1
        # return max(dp)
        sub = [nums[0]]
        for i in range(1, len(nums)):
            if sub[-1] < nums[i]:
                sub.append(nums[i])
            else:
                ind = bisect_left(sub, nums[i])
                sub[ind] = nums[i]
        return len(sub)
    
s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(s.lengthOfLIS([0,1,0,3,2,3]))
print(s.lengthOfLIS([7,7,7,7,7,7,7]))
print(s.lengthOfLIS([1,3,6,7,9,4,10,5,6]))