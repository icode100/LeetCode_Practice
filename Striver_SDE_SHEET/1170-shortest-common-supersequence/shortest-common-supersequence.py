class Solution:
    def shortestCommonSupersequence(self, string1: str, string2: str) -> str:
        dp = [[0 for _ in range(len(string2)+1)] for __ in range(len(string1)+1)]
        for i in range(len(string1)+1): dp[i][len(string2)] = len(string1)-i
        for j in range(len(string2)+1): dp[len(string1)][j] = len(string2)-j
        for i in range(len(string1)-1,-1,-1):
            for j in range(len(string2)-1,-1,-1):
                if string1[i]==string2[j]:
                    dp[i][j] = 1+dp[i+1][j+1]
                else:
                    dp[i][j] = 1+min(dp[i+1][j],dp[i][j+1])
        i,j,ans = 0,0,""
        while i<len(string1) and j<len(string2):
            if string1[i]==string2[j]:
                ans+=string1[i]
                i+=1
                j+=1
            else:
                if dp[i+1][j]<dp[i][j+1]: 
                    ans+=string1[i]
                    i+=1
                else:
                    ans+=string2[j]
                    j+=1
        if i<len(string1): ans+=string1[i:]
        if j<len(string2): ans+=string2[j:]
        return ans
        

        



