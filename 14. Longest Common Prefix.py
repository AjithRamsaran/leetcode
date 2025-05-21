#time taken to solve: 15 mins
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        strs = sorted(strs)
        first = strs[0]
        last = strs[len(strs) -1]
        c = 0
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            c += 1
        return first[:c]
           
