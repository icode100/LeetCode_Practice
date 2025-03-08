class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        count = [1]*n
        lis,ans = 0,0
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]: 
                    if 1+dp[j]>dp[i]:
                        dp[i] = 1+dp[j]
                        count[i] = count[j]
                    elif 1+dp[j]==dp[i]: count[i]+=count[j]                    
            if dp[i]>lis:
                lis = dp[i]
                ans = count[i]
            elif dp[i]==lis: ans+=count[i]
        return ans