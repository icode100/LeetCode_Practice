class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)&1: return False
        target = sum(nums)//2
        N = len(nums)
        dp = [[False for _ in range(target+1)] for _ in range(N+1)]
        for i in range(N+1):dp[i][0] = True
        for i in range(1,N+1):
            for tar in range(1,target+1):
                dp[i][tar] = dp[i-1][tar] or (dp[i-1][tar-nums[i-1]] if nums[i-1]<=tar else False)
        return dp[N][target]

        # @cache
        # def recursion(index,target):
        #     if target==0: return True
        #     if index<0: return False
        #     return recursion(index-1,target) or (recursion(index-1,target-nums[index]) if nums[index]<=target else False)
        # return recursion(N-1,target)


