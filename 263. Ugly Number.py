class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n% 2 == 0:
            n//= 2
        while n% 3 == 0:
            n//= 3
        while n% 5 == 0:
            n//= 5
        return n== 1
    
s = Solution()
print(s.isUgly(6))
print(s.isUgly(4))
print(s.isUgly(14))
print(s.isUgly(11))
