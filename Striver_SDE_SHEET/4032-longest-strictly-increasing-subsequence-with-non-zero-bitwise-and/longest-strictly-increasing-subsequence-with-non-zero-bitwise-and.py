class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        def lis(nums):
            lisvals = list()
            for num in nums:
                idx = bisect_left(lisvals,num)
                if idx==len(lisvals):
                    lisvals.append(num)
                else:
                    lisvals[idx] = num
            return len(lisvals)
        ans = 0
        for i in range(32):
            ans = max(
                ans,
                lis([num for num in nums if (num&(1<<i))!=0])
            )
        return ans