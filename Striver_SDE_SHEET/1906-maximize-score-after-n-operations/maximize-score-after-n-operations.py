class Solution:
    def maxScore(self, nums: List[int]) -> int:
        N = len(nums)>>1
        @cache
        def recursion(index,mask):
            if index>N: return 0
            ans = 0
            for i in range(N<<1):
                if (1<<i)&mask: continue
                for j in range(N<<1):
                    if i==j or (1<<j)&mask: continue
                    ans =  max(ans,(gcd(nums[i],nums[j])*index) + recursion(index+1,mask|(1<<i)|(1<<j)))
            return ans
        return recursion(1,0)