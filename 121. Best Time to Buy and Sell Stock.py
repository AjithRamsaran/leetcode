#time taken solve: 10 mins
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        mini = prices[0]
        for i in range(1, len(prices)):
            # if prices[i] < mini:
            #     mini = prices[i]
            mini = min(mini,prices[i] )
            # if prices[i] - mini > maxi:
            #     maxi = prices[i] - mini
            maxi = max(maxi,prices[i] - mini )
        return maxi
        
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,4,3,1]))
print(s.maxProfit([1,2,3,4,5]))