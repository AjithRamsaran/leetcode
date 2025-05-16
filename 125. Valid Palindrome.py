#time taken to solve: 30 mins
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= re.sub(r"[^a-zA-Z0-9]",'', s)
        n = len(s)
        for i in range(n//2):
            if s[i].lower() != s[n-i-1].lower():
                return False
        return True
        # n = len(s)
        # l = 0
        # r = n - 1
        # while l < r:
        #     if not s[l].isalnum():
        #         l += 1
        #         continue
        #     if not s[r].isalnum():
        #         r -= 1
        #         continue
        #     if s[l].lower() != s[r].lower():
        #         return False
        #     l += 1
        #     r -= 1
        # return True

s = Solution()
print(s.isPalindrome("MALAY ALAm"))
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("raceacar"))
print(s.isPalindrome(" "))