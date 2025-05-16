class Solution:
    def reverseBits(self, n: int) -> int:
        total = 0
        for _ in range(32):
            b = n & 1
            n = n << 1
            total = (total << 1) | b
        return total