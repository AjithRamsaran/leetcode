#time taken to solve and understanding: 1 hr+
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]

        # wordDict = set(wordDict)
        # memo = {}
        # def check(l, memo):
        #     if l == len(s):
        #         return True
        #     if l in memo:
        #         return memo[l]
        #     for i in range(l , len(s) + 1):
        #         if s[l:i] in wordDict:
        #             if check(i,memo):
        #                 memo[l] = True
        #                 return True
        #     memo[l] = False
        #     return False
        # return check(0,memo)