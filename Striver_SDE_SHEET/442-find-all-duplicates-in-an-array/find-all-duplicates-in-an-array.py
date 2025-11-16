class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = list()
        for num in nums:
            idx = abs(num)-1
            if idx<N and nums[idx]<0: ans.append(abs(num))
            if idx<N: nums[idx] = -abs(nums[idx])
        return ans
        