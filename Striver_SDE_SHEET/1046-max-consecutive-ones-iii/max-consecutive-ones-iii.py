class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        ans = 0
        N = len(nums)
        for r in range(N):
            k-=int(nums[r]==0)
            while k<0:
                k+=int(nums[l]==0)
                l+=1
            ans = max(ans,r-l+1)
        return ans