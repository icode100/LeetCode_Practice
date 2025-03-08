class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        def fx(nums):
            n = len(nums)
            current = 0
            prev = 0
            for i in range(n-1,-1,-1):
                temp = max(nums[i]+prev,current)
                prev = current
                current = temp
            return current
        return max(fx(nums[:-1]),fx(nums[1:]))
