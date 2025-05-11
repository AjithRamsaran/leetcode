from collections import Counter
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        given = defaultdict(int)
        lt = len(t)
        ls = len(s)
        left = 0
        have = 0
        ansLeft = -1
        minLen = float("inf")
        for right, ch in enumerate(s):
            given[ch] += 1
            if ch in need and given[ch] == need[ch]:
                have += 1
            while have == lt:
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    ansLeft = left
                given[s[left]] -= 1
                if s[left] in need and given[s[left]] < need[s[left]]:
                    have -= 1
                left += 1
        return s[ansLeft: ansLeft + minLen] if ansLeft != -1 else ""
                
                
        

s = Solution()
print(s.minWindow("ADOBECODEBANC","ABC"))
print(s.minWindow("a","a"))
print(s.minWindow("a","aa"))