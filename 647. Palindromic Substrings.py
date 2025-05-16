#time taken to solve: 10 mins
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def expand_around(l,r):
            nonlocal count
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        for i in range(len(s)):
            expand_around(i, i)
            expand_around(i, i + 1)
        return count
    
s = Solution()
print(s.countSubstrings("abc"))