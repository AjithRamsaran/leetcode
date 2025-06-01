#time taken to solve: 2.30 hrs
from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        nCol = len(heights[0])
        nRow = len(heights)
        pac, atl = set(), set()

        def dfs(r, c, visit, value):
            if ((r, c) in visit) or r < 0 or r == nRow or c < 0 or c == nCol or heights[r][c] < value:
                return
            visit.add((r, c))
            dfs(r, c - 1, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r + 1, c, visit, heights[r][c])
            

        for c in range(nCol):
            dfs(0, c, pac, heights[0][c])
            dfs(nRow - 1, c, atl, heights[nRow - 1][c])
        
        for r in range(nRow):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, nCol - 1, atl, heights[r][nCol - 1])
        merge = pac.intersection(atl)
        res = []
        for s in merge:
            res.append(list(s))
        return res