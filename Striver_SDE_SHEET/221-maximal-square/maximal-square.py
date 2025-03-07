class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix),len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]

        ans = 0
        for i in range(n):
            dp[0][i] = int(matrix[0][i])
            if ans ==0 and dp[0][i] == 1: ans = 1
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            if ans == 0 and dp[i][0]==1: ans = 1
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] =="1": 
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    ans = max(ans,dp[i][j]**2)
        print(dp)
        return ans 


