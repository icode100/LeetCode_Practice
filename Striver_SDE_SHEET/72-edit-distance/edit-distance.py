class Solution(object):
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)

        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for j in range(n+1):
            dp[0][j]= j
        for i in range(m+1):
            dp[i][0] = i
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    insert = 1+dp[i][j-1]
                    delete = 1+dp[i-1][j]
                    replace = 1+dp[i-1][j-1]
                    dp[i][j] = min(insert,replace,delete)
        return dp[m][n]