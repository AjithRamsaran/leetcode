#time taken solve: 10 mins
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        a = 1
        b = 2
        while(n - 2 >0):
            a, b = b, a + b
            n -= 1
        return b
s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(5))
print(s.climbStairs(45))
print(s.climbStairs(1))