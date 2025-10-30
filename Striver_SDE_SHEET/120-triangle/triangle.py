class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [[0]*m for i in range(m)]
        dp[0][0] = triangle[0][0]
        for i in range(1,m): dp[i][0] += dp[i-1][0]+triangle[i][0]
        for x in range(1,m):
            for y in range(1,x+1):
                dp[x][y] = triangle[x][y]+min(dp[x-1][y] if y<x else inf,dp[x-1][y-1])
        # print(dp)
        return min(dp[-1])