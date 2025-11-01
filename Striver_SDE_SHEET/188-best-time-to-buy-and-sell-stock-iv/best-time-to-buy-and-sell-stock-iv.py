class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        N = len(prices)
        K = k
        dp = [[[0 for _ in range(K+1)] for _ in range(2)] for _ in range(N+1)]
        for index in range(N-1,-1,-1):
            for  flag in [0,1]:
                for cap in range(1,K+1):
                    skip = dp[index+1][flag][cap]
                    if flag: dp[index][flag][cap] = max(-prices[index]+dp[index+1][not flag][cap], skip)
                    else: dp[index][flag][cap] = max(prices[index]+dp[index+1][not flag][cap-1],skip)
        return dp[0][1][K]