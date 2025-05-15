from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        

    def addNum(self, num: int) -> None:
        heappush(self.maxheap, -num)
        if self.maxheap and self.minheap and -self.maxheap[0] > self.minheap[0]:
            heappush(self.minheap, -heappop(self.maxheap))

        if len(self.maxheap) > len(self.minheap) + 1:
            heappush(self.minheap, -heappop(self.maxheap))

        if len(self.maxheap) + 1 < len(self.minheap):
                heappush(self.maxheap, -heappop(self.minheap))

        

    def findMedian(self) -> float:
        #print(self.maxheap)
        #print(self.minheap)
        if (len(self.minheap) + len(self.maxheap)) % 2 == 0:
            #print("total a",(self.minheap[0] + (-self.maxheap[0])) )
            return (self.minheap[0] + (-self.maxheap[0]))/2.0
        else:
            return self.minheap[0] if len(self.minheap) > len(self.maxheap) else -self.maxheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()