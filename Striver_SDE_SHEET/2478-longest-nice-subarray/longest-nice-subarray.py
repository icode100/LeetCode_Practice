class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        mask = 0
        l = 0
        for r in range(n):
            while (mask&nums[r])!=0:
                mask^=nums[l]
                l+=1
            mask|=nums[r]
            ans = max(ans,r-l+1)
        return ans
        



            