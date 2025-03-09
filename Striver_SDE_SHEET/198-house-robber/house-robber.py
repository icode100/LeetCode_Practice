class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        def recursion(index,nums):
            if index>=len(nums): return 0
            if index in dp: return dp[index]
            dp[index] =  max(nums[index]+recursion(index+2,nums), recursion(index+1,nums))
            return dp[index]
        return recursion(0,nums)


