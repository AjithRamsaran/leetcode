#time taken to solve 4 hrs
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # def bs():
        #     l = 0
        #     n = len(intervals)
        #     r = n - 1
        #     m = (l + r) // 2
        #     while l < r:
        #         m = (l + r) // 2
        #         print(newInterval[0], intervals[m][0])
        #         if newInterval[0] > intervals[m][0]:
        #             l = m + 1
        #         else:
        #             r = m 
        #     return l
        #index = bs()
       # intervals.insert(index, newInterval)
        #print(intervals)
        i = 0
        res = []
        n = len(intervals)

        while i < n and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1

        while i < n and newInterval[1] >= intervals[i][0]:    
            newInterval[0]  = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
            #print(res)
        res.append(newInterval)
        res.extend(intervals[i:])
        return res
        