class Solution:
    def numTilings(self, n: int) -> int:
        dp = [0]*(max(5,n+1))
        mod = int(1e9+7)
        dp[1], dp[2], dp[3], dp[4] = 1, 2, 5, 11
        for i in range(5,n+1): dp[i] = (((2*dp[i-1])%mod)+(dp[i-3]%mod))%mod
        return dp[n]
