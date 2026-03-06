class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        '''
        * sort
        * dp state = dp(i,diff,last,rem) use pick and notpick if rem==0 return diff where diff is the min difference
        '''
        mod = int(1e9+7)
        nums.sort()
        ans = 0
        N = len(nums)
        @cache
        def recursion(i,diff,last,rem):
            if rem==0:
                return diff if diff!=inf else 0
            if i==N: return 0

            pick = recursion(i+1,min(abs(nums[i]-last),diff),nums[i],rem-1)
            notpick = recursion(i+1,diff,last,rem)
            return (pick+notpick)%mod
        return recursion(0,inf,inf,k)