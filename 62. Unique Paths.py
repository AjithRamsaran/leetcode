class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [1] * n
        for i in range(m - 1):
            for j in range(n):
                paths[j] = paths[j] + (paths[j-1] if j - 1 >=0 else 0)
        return paths[n-1]


        #recursion with memoization
        # def canReach(i, j, memo):
        #     if i >= m or j >= n:
        #         return 0
            
        #     if memo[i][j] != -1:
        #         return memo[i][j]

        #     if i == m -1 and j == n -1:
        #         return 1

        #     down = canReach(i+1, j, memo)
        #     right = canReach(i, j + 1,memo)
        #     memo[i][j] = down + right
        #     return memo[i][j]
        # return canReach(0,0, [[-1 for i in range(n)] for k in range(m)])
