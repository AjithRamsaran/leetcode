class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF  # 32 bit mask
        maxInt = 2**31 - 1

        while b != 0:
            sum = (a ^ b) & mask # contain to 32 bits
            carry = (a & b) & mask # contain to 32 bits
            a = sum
            b = carry << 1
        
        return a if a <= maxInt else ~(a ^ mask)
        # mask = 0xFFFFFFFF
        # maxInt = 2**31 - 1
        # c = -1
        # while b != 0:
        #     c = (a&b) & mask 
        #     a = a^b  & mask 
        #     b = (c)<<1  
        # return a if a <= maxInt else ~(a ^ mask)
        
s = Solution()
print(s.getSum(-1,2))