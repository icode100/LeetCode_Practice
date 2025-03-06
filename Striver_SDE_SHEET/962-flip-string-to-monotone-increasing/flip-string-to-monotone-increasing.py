class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp = defaultdict(lambda:defaultdict(int))
        for i in range(len(s)-1,-1,-1):
            if s[i]=='0':
                dp[i][0] = 1+dp[i+1][0]
                dp[i][1] = min(1+dp[i+1][0],dp[i+1][1])
            else:
                dp[i][0] = dp[i+1][0]
                dp[i][1] = min(1+dp[i+1][1],dp[i+1][0])
        return min(dp[0][0],dp[0][1])

        
