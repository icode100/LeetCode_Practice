class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        minsum = 0
        sum = 0
        ans = -sys.maxsize-1
        for num in nums:
            sum+=num
            ans = max(ans,sum-minsum)
            minsum = min(minsum,sum)
        return ans
