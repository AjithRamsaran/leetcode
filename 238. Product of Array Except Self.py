#time taken solve: 45 mins
#Logic: store previous product to current index in an array in left to right iteration. similarly do the right to left. multiple both values thats the answer. 
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        product = 1
        for i in range(len(nums)):
            result[i] = product
            product *= nums[i]
        product = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= product
            product *= nums[i]
        return result
    
s = Solution()
print(s.productExceptSelf([1,2,3,4]))
print(s.productExceptSelf([-1,1,0,-3,3]))