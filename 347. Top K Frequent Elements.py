from collections import defaultdict
from heapq import heappush, heappop
import itertools
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        map = defaultdict(int)
        counter = itertools.count()
        for i in nums:
            map[i] += 1
        maxHeap = []
        print(map)
        for i in map:
            print(i)
            heappush(maxHeap, (map[i],i,next(counter), ))
            if(len(maxHeap)) > k:
                heappop(maxHeap)
    
        res = []
        while k >0:
           val,i, _  = heappop(maxHeap)
           res.append(i)
           k -= 1
        return res
        
        
s = Solution()
print(s.topKFrequent([1,1,1,2,2,3,1], 2))
print("New")
print(s.topKFrequent([3,3,2,2,4,4,4], 2))