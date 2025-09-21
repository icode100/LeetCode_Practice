class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prevmin = prices[0]
        ans = 0
        for i in range(1,len(prices)):
            prevmin = min(prevmin,prices[i])
            ans = max(ans,prices[i]-prevmin)
        return ans