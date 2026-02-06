class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        l = 0
        ans = 0
        for r in range(N):
            while l<r and nums[l]*k<nums[r]:
                l+=1
            ans = max(ans,r-l+1)
        return N-ans
            