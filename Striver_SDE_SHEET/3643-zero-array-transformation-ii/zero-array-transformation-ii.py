class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        dp = [0]*n
        current=0
        ans = 0
        for i in range(n):
            while current+dp[i]<nums[i]:
                ans+=1
                if ans>len(queries): return -1
                s,e,v = queries[ans-1]
                if e>=i:
                    dp[max(i,s)]+=v
                    if e+1<n: dp[e+1]-=v
            current+=dp[i]
        return ans
            


