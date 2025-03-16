class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        def check(mid):
            dp = [0]*n
            current = 0
            for s,e,v in queries[:mid]:
                dp[s]+=v
                if e+1<n: dp[e+1]-=v
            for i,num in enumerate(dp):
                current+=num
                if current<nums[i]: return False
            return True
        left,right = 0,len(queries)
        while left<=right:
            mid = (left+right)//2
            if check(mid): right = mid-1
            else: left = mid+1
        return left if left<=len(queries) else -1

