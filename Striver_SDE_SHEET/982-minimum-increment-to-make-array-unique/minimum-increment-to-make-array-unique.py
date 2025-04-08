class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        ans = 0
        for i in range(1,N):
            if nums[i]<=nums[i-1]:
                ans+=(nums[i-1]-nums[i]+1)
                nums[i] = nums[i-1]+1
        # print(nums)
        return ans
