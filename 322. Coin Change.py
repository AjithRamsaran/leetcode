from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        a = [float('inf')] * (amount +1)
        #print(a)
        
        for j in range(amount + 1):
            if j % coins[0] == 0:
                a[j] = j // coins[0]

        for i in range(1, len(coins)):
            for j in range (amount +1):
                # if coins[i] > j:
                #     a[i][j] = a[j]
                if coins[i] <= j:
                    a[j] = min(a[j], 1 + a[j-coins[i]])
        #print(a)
        res = a[amount]
        return res if res != float("inf") else -1
        

        # minVal = float("inf")
        # def rec(coins, n , amount, count):
        #     nonlocal minVal
        #     if count > minVal:
        #         return 0
        #     if amount == 0:
        #         if count < minVal:
        #             minVal = count
        #         return 1
        #     if amount < 0 or n == 0:
        #         return 0
        #     return rec(coins, n, amount - coins[n -1], count + 1) + rec(coins, n - 1, amount, count)
        # res = rec(coins, len(coins), amount, 0) 
        # return minVal if minVal != float("inf") else -1
    
#print(sys.getrecursionlimit())
#sys.setrecursionlimit(3000)
s = Solution()
print(s.coinChange([1,2,5], 11))
print(s.coinChange([2], 3))
print(s.coinChange([1], 0))
print(s.coinChange([2,3,5,10], 15))
print(s.coinChange([3,7,405,436], 8839))