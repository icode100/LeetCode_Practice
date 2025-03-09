class Solution:
    def numberOfAlternatingGroups(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        ans = 0
        for r in range(1,n+k-1):
            if nums[r%n]==nums[(r-1)%n]: 
                l = r
                continue
            elif r-l+1>=k: ans+=1
        return ans
