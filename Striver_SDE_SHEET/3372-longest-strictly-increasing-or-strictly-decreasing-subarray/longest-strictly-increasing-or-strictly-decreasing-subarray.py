class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        inc,dec,ans = 0,0,0
        for i in range(1,n):
            if nums[i]==nums[i-1]: 
                inc=0
                dec=0
                continue
            elif nums[i]>nums[i-1]: 
                dec = 0
                inc+=1
                # print(inc)
                ans = max(ans,inc)
            elif nums[i]<nums[i-1]:
                inc = 0
                dec+=1
                if dec==2: print(i)
                ans = max(ans,dec)
        return ans+1