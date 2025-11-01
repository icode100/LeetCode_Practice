class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [[0,0] for _ in range(N+1)]
        for index in range(N-1,-1,-1):
            for flag in [True,False]:
                if flag:
                    dp[index][flag] = max(prices[index]+dp[index+1][not flag],dp[index+1][flag])
                else:
                    dp[index][flag] = max(-prices[index]+dp[index+1][not flag],dp[index+1][flag])
        return dp[0][False]

