class Solution:
    def __init__(self):
        self.INT_MAX = sys.maxsize
        self.INT_MIN = -sys.maxsize-1

    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        min_prefix = [self.INT_MAX]*k
        # min_prefix[0] = 0

        N = len(nums)
        ans = self.INT_MIN
        current = 0
        
        for r,num in enumerate(nums):
            current += num

            if (r+1)%k==0: ans = max(ans,current)

            l = (r+1)%k
            ans = max(ans,current-min_prefix[l])
        
            min_prefix[(r+1)%k] = min(min_prefix[(r+1)%k], current)
            
        return ans