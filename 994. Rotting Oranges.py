#time taken to solve: 1 hour
from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [[0,-1], [0, 1], [-1, 0], [1, 0]]
    
        q = deque()

        rotton = 0
        fresh = 0
        for r in range(m):
            for c in range(n):
                if  grid[r][c] == 2:
                    q.append((r,c))
                    rotton += 1
                if grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        
        if not q:
            return -1

        count = -1
        while q:
            count += 1
            qLen = len(q)
            for _ in range(qLen):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r >= 0 and c >= 0 and r < m and c < n  and grid[r][c] == 1:
                        q.append((r,c))
                        grid[r][c] = 2

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return -1
        return count 
