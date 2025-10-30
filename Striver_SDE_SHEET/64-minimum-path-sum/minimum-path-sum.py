class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1,m): dp[i][0] = dp[i-1][0]+grid[i][0]
        for i in range(1,n): dp[0][i] = dp[0][i-1]+grid[0][i]
        for x in range(1,m):
            for y in range(1,n):
                dp[x][y] = min(dp[x-1][y],dp[x][y-1])+grid[x][y]

        return dp[m-1][n-1]