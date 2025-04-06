class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        N = len(nums)

        dp = [deque([i]) for i in nums]
        ans = list()
        for i in range(N):
            for j in range(i):
                if nums[i]%nums[j]==0:
                    dp[j].append(nums[i])
                    temp = dp[j].copy()
                    dp[j].pop()
                    if len(temp)>len(dp[i]): dp[i] = temp
                    
            ans = dp[i] if len(dp[i])>len(ans) else ans
        return list(ans)
        # @cache
        # def recursion(i):
        #     if i>=N: return []
        #     ans = [nums[i]]
        #     for j in range(i+1,N):
        #         if nums[j]%nums[i]==0:
        #             temp = [nums[i]]+recursion(j)
        #             ans = temp if len(temp)>len(ans) else ans
        #     return ans
        # ans = list()
        # for i in range(N):
        #     temp = recursion(i)
        #     ans = temp if len(temp)>len(ans) else ans
        # return ans
            