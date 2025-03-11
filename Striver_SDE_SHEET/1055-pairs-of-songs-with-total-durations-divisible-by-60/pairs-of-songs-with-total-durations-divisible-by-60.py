class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dp,ans = {},0
        for i in time:
            ans+=dp.get((60-(i%60))%60, 0)
            dp[i%60] = dp.get(i%60,0)+1
        return ans