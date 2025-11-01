class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        count = [1]*N
        dp = [1]*N
        for i in range(N):
            for j in range(i):
                if nums[i]>nums[j]:
                    if dp[i]==dp[j]+1: count[i]+=count[j]
                    elif dp[i]<dp[j]+1:
                        dp[i] = dp[j]+1
                        count[i] = count[j]
        lis = max(dp)
        return sum([count[i] if dp[i]==lis else 0 for i in range(N)])