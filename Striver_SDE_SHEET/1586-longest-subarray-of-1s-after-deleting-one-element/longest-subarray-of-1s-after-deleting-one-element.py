class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        ans,zero = 0,0
        l = 0
        for r in range(N):
            zero+=int(nums[r]==0)
            while zero>1:
                zero-=int(nums[l]==0)
                l+=1
            ans = max(ans,r-l+1)
        return ans-1
