class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp_i, dp_i_1, dp_i_2 = 0,0,0
        for i in range(n-1,-1,-1):
            dp_i = max(nums[i]+dp_i_2, dp_i_1)
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
        return dp_i


