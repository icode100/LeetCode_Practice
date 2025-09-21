class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -sys.maxsize
        sum = 0
        for num in nums:
            sum+=num
            ans = max(sum,ans)
            if sum<0: sum=0
        return ans