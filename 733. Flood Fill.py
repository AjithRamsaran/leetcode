#time taken to solve: 20 mins (read solution and then wrote the code)
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        m = len(image)
        n = len(image[0])

        originalColor = image[sr][sc]
                
        def fill(r,c):
            if (r < 0 or r >= m) or (c < 0 or c >= n):
                return
            if image[r][c] != originalColor:
                return
            image[r][c] = color
            fill(r-1, c)
            fill(r, c-1)
            fill(r+1, c)
            fill(r, c+1)

        fill(sr, sc)
        return image