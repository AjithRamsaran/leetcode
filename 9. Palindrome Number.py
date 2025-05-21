class Solution:
    def isPalindrome(self, x: int) -> bool:
        #approach 1
        # x = str(x)
        # return x == x[::-1]
        if x < 0:
            return False
        total = 0
        i = 1
        temp = x
        while x > 0:
            total = (total * 10) + (x % 10)
            x = x//10
            i = i * 10
        return temp == total