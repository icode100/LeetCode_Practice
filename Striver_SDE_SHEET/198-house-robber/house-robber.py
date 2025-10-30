class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0]*(N+2)
        for i in range(N-1,-1,-1):
            dp[i] = max(dp[i+1],nums[i]+dp[i+2])
        return dp[0]
