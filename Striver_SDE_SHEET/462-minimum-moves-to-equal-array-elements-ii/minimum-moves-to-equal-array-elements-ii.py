class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        median = nums[n>>1]
        ans  =0
        for i in nums:
            ans+=abs(i-median)
        return ans