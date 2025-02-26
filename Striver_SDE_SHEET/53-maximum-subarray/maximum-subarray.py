class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        minsum = 0
        ans = -1e6
        current = 0
        for i in nums: 
            current+=i
            ans = max(ans,current-minsum)
            minsum = min(minsum,current)
        return ans