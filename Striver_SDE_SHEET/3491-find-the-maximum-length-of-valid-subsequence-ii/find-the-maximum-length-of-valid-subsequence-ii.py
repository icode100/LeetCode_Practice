class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda x:x%k,nums))
        dp = {}
        N = len(nums)
        for i in range(N):
            dp[i] = {}
            for j in range(i):
                dp[i][nums[i]+nums[j]] = 1+dp[j].get(nums[i]+nums[j],1)
        return max(max(dp[i].values()) for i in dp.keys() if len(dp[i])>0)

