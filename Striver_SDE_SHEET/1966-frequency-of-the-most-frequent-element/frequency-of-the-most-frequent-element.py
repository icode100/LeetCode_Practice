class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        currsum = 0
        ans = l = 0
        for r in range(len(nums)):
            currsum+=nums[r]
            while ((nums[r]*(r-l+1))-currsum)>k:
                currsum-=nums[l]
                l+=1
            ans = max(ans,r-l+1)
        return ans

