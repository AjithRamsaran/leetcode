from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = defaultdict(int)
        l = 0 
        maxi = 0
        result = 0
        for r, ch in enumerate(s):
            map[ch] += 1
            maxi = max(maxi, map[ch])
            if (r - l + 1) - maxi > k:
                map[s[l]] -= 1
                l +=1
            result = max(result, r-l+1)      
        return result

s = Solution()
print(s.characterReplacement("ABAB", 2))
print(s.characterReplacement("AABABBA", 1))