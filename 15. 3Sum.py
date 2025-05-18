#time taken solve: 45 mins + learning best solutions
from typing import List
from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i -1]:
                continue
            target = -nums[i]
            left, right = i + 1, n - 1
            while left < right:
                if  nums[left] + nums[right] == target:
                    res.append([nums[i], nums[left], nums[right]])
                    while  left < right and     nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right]  == nums[right - 1]:
                        right -= 1
                if nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return res
        
        
        # def modifiedList(nums):
        #     m = defaultdict(int)
        #     modifiedNums = []
        #     for i in nums:
        #         if m[i] <= 3:
        #             modifiedNums.append(i)
        #         m[i] += 1
        #     return modifiedNums
        # nums = modifiedList(nums)
        # nums = sorted(nums)
        # s = set()
        # l = []
        # def twoSum(arr, target):
        #     m = set()
        #     li = []
        #     for i in arr:
        #         if target - i in m:
        #             li.append([i, target - i])
        #         m.add(i)
        #     return li
        # for i,val in enumerate(nums):
        #    res = twoSum(nums[i+1:], -val)
        #    if res:
        #         for j in res:
        #             j.insert(0,val)
        #             if tuple(j) not in s:
        #                 l.append(j)
        #                 s.add(tuple(j))
        # return l
s =  Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0,1,1]))
print(s.threeSum([0,0,0]))
print(s.threeSum([-1,0,1,0]))
print(s.threeSum([-1,0,1,2,-1,-4]))