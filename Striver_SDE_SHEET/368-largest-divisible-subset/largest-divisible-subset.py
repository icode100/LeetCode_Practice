class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        N = len(nums)
        @cache
        def recursion(i,prev):
            if i>=N: return []
            notpick = recursion(i+1,prev)
            pick = []
            if nums[i]%prev==0:
                pick = [nums[i]]+recursion(i+1,nums[i])
            return pick if len(pick)>len(notpick) else notpick
        return recursion(0,1)
            