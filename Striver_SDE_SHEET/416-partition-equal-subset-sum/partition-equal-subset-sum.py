class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        total = sum(nums)
        if total&1: return False
        target = total//2
        dp = [[False for _ in range(total)] for _ in range(N+1)]
        for i in range(N+1): dp[i][target]=True
        for i in range(N-1,-1,-1):
            for current in range(total):
                dp[i][current] = dp[i+1][current] or (dp[i+1][current+nums[i]] if current+nums[i]<=target else False)
        return dp[0][0]


        # @cache
        # def recursion(index, current):
        #     if current==(total//2): return True
        #     if index==N: return current==(total//2)
        #     notpick = recursion(index+1,current)
        #     pick = recursion(index+1,current+nums[index]) if nums[index]+current<=(total//2) else False
        #     return pick or notpick
        # return recursion(0,0)
