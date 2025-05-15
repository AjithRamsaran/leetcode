class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0
        
        for i in range(32):
            if (n >> i) & 1:
                count += 1
        return count 
        
        count = 0
        while (n != 1):
            if n % 2 == 1:
                count +=1
            n = n // 2
        return count + 1
    

    
s = Solution()
print(s.hammingWeight(2147483645)) #output 2147483645
print(s.hammingWeight(128)) # 1
print(s.hammingWeight(11)) # 3