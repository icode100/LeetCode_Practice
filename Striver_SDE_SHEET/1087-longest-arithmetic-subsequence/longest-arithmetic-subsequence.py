class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        for i in range(n):
            dp[i] = {}
            for j in range(i):
                dp[i][nums[i]-nums[j]] = 1+dp[j].get(nums[i]-nums[j],1)
                
        return max(max(dp[i].values()) for i in range(n) if len(dp[i])>0)