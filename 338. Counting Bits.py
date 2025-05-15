from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:

        l = [0]
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = offset * 2
            l.append(1 + l[i - offset])
        return l
s = Solution()
print(4)
print(5)