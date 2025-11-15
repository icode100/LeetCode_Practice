class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            if nums[i]<=0 or nums[i]>N: nums[i] = N+1
        for num in nums:
            idx = abs(num)-1
            if idx<N: nums[idx] = -abs(nums[idx])
        for i in range(N):
            if nums[i]>0: return i+1
        return N+1