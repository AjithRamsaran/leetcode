class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key = lambda x:x[1])
        arrowCount = 1
        prevEnd = points[0][1]
        for i in range(1,len(points)):
            if points[i][0] > prevEnd:
                arrowCount+=1
                prevEnd = points[i][1]
        return arrowCount
    
s = Solution()
print(s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(s.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
print(s.findMinArrowShots([[-2147483648,2147483647]]))
print(s.findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))
print(s.findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]))
