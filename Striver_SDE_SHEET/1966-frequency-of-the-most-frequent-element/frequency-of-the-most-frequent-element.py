class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr,n = 0,len(nums)
        left,right = 0,0
        ans = -sys.maxsize-1
        for right in range(n):
            curr+=nums[right]
            while left<right and nums[right]*(right-left+1)-curr>k:
                curr-=nums[left]
                left+=1
            ans = max(ans,right-left+1)
        return ans
            

