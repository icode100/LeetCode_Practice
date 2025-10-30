class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0] = grid[0]
        for i in range(1,m):
            for j in range(n):
                dp[i][j] = grid[i][j]+min(dp[i-1][j], dp[i-1][j-1] if j-1>-1 else inf, dp[i-1][j+1] if j+1<n else inf)
        return min(dp[-1])
                