class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        N,M = len(str1),len(str2)
        dp = [[0]*(M+1) for _ in range(N+1)]
        for i in range(1,N+1):
            for j in range(1,M+1):
                if str1[i-1]==str2[j-1]: dp[i][j] = dp[i-1][j-1]+1
                else: dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        ans = ""
        i=N
        j=M
        while i>0 and j>0:
            if str1[i-1]==str2[j-1]:
                ans+=str1[i-1]
                i-=1
                j-=1
            else:
                if dp[i-1][j]>dp[i][j-1]:
                    ans+=str1[i-1]
                    i-=1
                else:
                    ans+=str2[j-1]
                    j-=1
        while i>0:
            ans+=str1[i-1]
            i-=1
        while j>0:
            ans+=str2[j-1]
            j-=1
        return ans[::-1]
