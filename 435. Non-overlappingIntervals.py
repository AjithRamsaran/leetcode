class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x: x[0] )
        answer = 0
        prev = intervals[0][1]

        for i in range(1,len(intervals)):
            if prev > intervals[i][0]:
                answer += 1
                prev = min(prev, intervals[i][1])
            else:
                prev = intervals[i][1]

#         while len(intervals) != pointer :
#             if prev > intervals[pointer][0]:
#                 answer += 1
#                 if(intervals[pointer][1] >  prev):
# #                    intervals.remove(intervals[pointer])
#                     prev = intervals[pointer - 1 ][1]
#                 else:
# #                    intervals.remove(intervals[pointer -1])
#                     prev = intervals[pointer][1]
#                 pointer += 1
#             else:
#                 prev = intervals[pointer][1]
#                 pointer += 1
        return answer
s = Solution()
print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(s.eraseOverlapIntervals([[1,2],[2,3]]))
print(s.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))